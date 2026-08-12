"""Multi-Agent SDR System powered by Google Gemini 2.5 Flash."""
import json
import os
from typing import Dict, Any, List

class MultiAgentSDRSystem:
    def __init__(self, leads_filepath: str):
        self.leads_filepath = leads_filepath
        with open(leads_filepath, "r", encoding="utf-8") as f:
            self.leads = json.load(f)

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

    def lead_discovery_agent(self, lead_id: str) -> Dict[str, Any]:
        for lead in self.leads:
            if lead["lead_id"] == lead_id:
                return {
                    "lead_info": lead,
                    "status": "Enriched",
                    "notes": f"Enriched profile for {lead['contact_name']} at {lead['company']}"
                }
        return {}

    def qualification_agent(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        info = lead_data.get("lead_info", {})
        size = info.get("company_size", 0)
        tech = info.get("tech_stack", [])
        
        score = 0
        if size >= 100:
            score += 50
        elif size >= 30:
            score += 30
        else:
            score += 10
            
        if any(t in ["Python", "Kubernetes", "AWS", "GCP"] for t in tech):
            score += 40
            
        is_qualified = score >= 60
        return {
            "score": score,
            "is_qualified": is_qualified,
            "qualification_reason": "High ICP fit based on company size and modern tech stack." if is_qualified else "Low ICP match."
        }

    def personalization_agent(self, lead_data: Dict[str, Any]) -> Dict[str, Any]:
        info = lead_data.get("lead_info", {})
        api_key = self._get_gemini_key()
        if api_key:
            try:
                from google import genai
                client = genai.Client(api_key=api_key)
                prompt = (
                    f"You are a Sales Personalization Specialist Agent.\n"
                    f"Company: {info.get('company')}\n"
                    f"Industry: {info.get('industry')}\n"
                    f"News: {info.get('recent_news')}\n"
                    f"Tech Stack: {info.get('tech_stack')}\n\n"
                    f"Write a 1-sentence customized sales hook referencing their recent company growth."
                )
                resp = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                hook = resp.text.strip()
                return {
                    "personalized_hook": hook,
                    "target_pain_point": f"Scaling infrastructure efficiently while managing cloud costs."
                }
            except Exception as e:
                print(f"Gemini API Exception in SDR Personalization: {e}")

        news = info.get('recent_news', '')
        company = info.get('company', '')
        industry = info.get('industry', 'Tech')
        tech_stack = info.get('tech_stack', [])
        
        hook = f"I noticed that {company} recently {news.lower()}." if news else f"I've been following {company}'s impressive growth in the {industry} sector."
        
        # Dynamic Pain Point synthesis
        if "fintech" in industry.lower() or "financial" in industry.lower():
            pain_point = "scaling real-time data pipelines and fraud detection while maintaining low latency."
        elif "logistics" in industry.lower() or "supply" in industry.lower():
            pain_point = "optimizing regional distribution operations and supply chain visibility."
        elif "cloud" in industry.lower() or "infrastructure" in industry.lower():
            pain_point = "managing Kubernetes cluster costs and automating cloud infrastructure scaling."
        else:
            pain_point = f"scaling engineering infrastructure and optimizing modern stack ({', '.join(tech_stack[:2]) if tech_stack else 'cloud tools'})."

        return {
            "personalized_hook": hook,
            "target_pain_point": pain_point
        }

    def email_copywriter_agent(self, lead_data: Dict[str, Any], qual: Dict[str, Any], persona: Dict[str, Any]) -> Dict[str, Any]:
        info = lead_data.get("lead_info", {})
        api_key = self._get_gemini_key()
        if api_key:
            try:
                from google import genai
                client = genai.Client(api_key=api_key)
                prompt = (
                    f"You are an expert B2B SDR Email Copywriter.\n"
                    f"Recipient: {info.get('contact_name')}, {info.get('title')} at {info.get('company')}\n"
                    f"Personalized Hook: {persona['personalized_hook']}\n"
                    f"Pain Point: {persona['target_pain_point']}\n\n"
                    f"Draft a compelling 3-paragraph cold outreach email. Include a clear call to action."
                )
                resp = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                body = resp.text.strip()
                return {
                    "subject": f"Congratulations on {info.get('company')}'s expansion!",
                    "body": body
                }
            except Exception as e:
                print(f"Gemini API Exception in SDR Email Copywriter: {e}")

        contact = info.get('contact_name', 'there')
        title = info.get('title', 'Leader')
        company = info.get('company', 'your company')
        industry = info.get('industry', 'industry')

        body = (
            f"Hi {contact},\n\n"
            f"{persona['personalized_hook']}\n\n"
            f"As {title} at {company}, navigating growth in the {industry} space often brings challenges around {persona['target_pain_point']}\n\n"
            f"Our platform helps engineering teams streamline these operations and boost team velocity. Would you be open to a quick 15-minute introductory chat next Tuesday?\n\n"
            f"Best regards,\nSDR Automation Team"
        )
        return {"subject": f"Quick question regarding {company}'s expansion", "body": body}

    def human_approval_gate(self, email_draft: Dict[str, Any], auto_approve: bool = True) -> Dict[str, Any]:
        if auto_approve:
            return {"status": "APPROVED", "action": "Email queued for dispatch.", "draft": email_draft}
        return {"status": "REJECTED", "action": "Flagged for manual review.", "draft": email_draft}

    def process_lead(self, lead_id: str, auto_approve: bool = True) -> Dict[str, Any]:
        lead_data = self.lead_discovery_agent(lead_id)
        if not lead_data:
            return {"error": "Lead not found"}

        qual = self.qualification_agent(lead_data)
        if not qual["is_qualified"]:
            return {
                "lead_id": lead_id, "qualification": qual,
                "status": "DISQUALIFIED", "message": "Lead did not meet minimum ICP threshold."
            }

        persona = self.personalization_agent(lead_data)
        email = self.email_copywriter_agent(lead_data, qual, persona)
        gate_res = self.human_approval_gate(email, auto_approve=auto_approve)

        return {
            "lead_id": lead_id,
            "model_used": "gemini-2.5-flash",
            "qualification": qual,
            "personalization": persona,
            "email_draft": email,
            "approval_gate": gate_res
        }
