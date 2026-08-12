"""Visual QA and Image Retrieval Engine powered by Google Gemini 2.5 Flash."""
import json
import os
from typing import Dict, Any, List

class VisualQAEngine:
    def __init__(self, catalog_filepath: str):
        with open(catalog_filepath, "r", encoding="utf-8") as f:
            self.catalog = json.load(f)

    def _get_gemini_key(self) -> str:
        key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not key or not key.strip():
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            env_path = os.path.join(base_dir, ".env")
            if os.path.exists(env_path):
                with open(env_path, "r", encoding="utf-8") as f:
                    for line in f:
                        if line.startswith("GEMINI_API_KEY=") or line.startswith("GOOGLE_API_KEY="):
                            key = line.split("=", 1)[1].strip()
                            break
        return key.strip() if key else ""

    def retrieve_images(self, query: str, top_k: int = 2) -> List[Dict[str, Any]]:
        q_words = set(query.lower().split())
        scored = []
        for img in self.catalog:
            tags = set(img.get("tags", []))
            desc_words = set(img.get("description", "").lower().split())
            txt_words = set(img.get("extracted_text", "").lower().split())

            score = len(q_words.intersection(tags)) * 3 + len(q_words.intersection(desc_words)) * 2 + len(q_words.intersection(txt_words))
            scored.append((score, img))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [img for _, img in scored[:top_k]]

    def answer_visual_question(self, question: str) -> Dict[str, Any]:
        matched_images = self.retrieve_images(question)
        if not matched_images:
            return {
                "question": question,
                "answer": "No relevant visual assets found in catalog.",
                "retrieved_images": []
            }

        top_img = matched_images[0]

        api_key = self._get_gemini_key()
        if api_key:
            try:
                from google import genai
                client = genai.Client(api_key=api_key)
                prompt = (
                    f"You are a Vision-Language Assistant.\n"
                    f"Retrieved Visual Asset: {top_img['filename']}\n"
                    f"Description: {top_img['description']}\n"
                    f"OCR Text: {top_img['extracted_text']}\n\n"
                    f"User Question: {question}\n\n"
                    f"Provide an accurate grounded answer referencing the visual metadata."
                )
                resp = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                return {
                    "question": question,
                    "model_used": "gemini-2.5-flash",
                    "answer": resp.text.strip(),
                    "retrieved_images": matched_images
                }
            except Exception as e:
                print(f"Gemini Visual QA Exception: {e}")

        answer = f"Based on visual asset '{top_img['filename']}' ({top_img['description']}):\nExtracted details: {top_img['extracted_text']}"

        return {
            "question": question,
            "model_used": "Local Visual Engine",
            "answer": answer,
            "retrieved_images": matched_images
        }
