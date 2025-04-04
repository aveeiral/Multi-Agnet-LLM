from .agent_base import AgentBase

class SummarizeValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="SummarizeValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, original_text, summary):

        system_message = "You are an expert AI assisstant that validates summaries of medical texts."
        user_content = (
            "Given the original summary, assess whether the summary accurately capture the key points and is of high quality.\n"
            "Provide a brief analysis and rate the sanitized process on a scale of 1 to 5, where 5 indicates excellent quality.\n\n"
            f"Original Text: {original_text}:\n\n"
            f"Summary: \n{summary}\n\n"
            "Validations:"

        )



        messages = [
            {"role": "system", "content": system_message},
            {"role":"user",    "content": user_content}
        ]

        validation = self.call_openai(messages, max_tokens=512)
        return validation