from .agent_base import AgentBase

class SanitizeDataTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(name="SanitizeDataTool", max_retries=max_retries, verbose=verbose)

    def execute(self, medical_data):
        messages = [
            {"role": "system", "content": "You are an AI assistent that sanitizess medical data by removing Protected Health Information(PHI)."},
            {
                "role":"user",
                "content": (
                    "Remove all the PHI from the following data:\n\n"
                    f"{medical_data}\n\nSanitized Data:"
                )
            }
        ]   
        summary = self.call_openai(messages, max_tokens=500)
        return summary