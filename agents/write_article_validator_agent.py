from .agent_base import AgentBase

class WriteArticleValidator(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(name="WriteArticleValidatorAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, topic, article):

        system_message = "You are an expert AI assisstant that validates research articles."
        user_content = (
            "Given the topic and the article, assesses whether the article comprehensively covers the topic, follows a logical structure, and maintains academic standards.\n"
            "Provide a brief analysis and rate the article on a scale of 1 to 5, where 5 indicates excellent quality.\n\n"
            f"Topic: {topic}:\n\n"
            f"Article: \n{article}\n\n"
            "Validations:"

        )



        messages = [
            {"role": "system", "content": system_message},
            {"role":"user",    "content": user_content}
        ]

        validation = self.call_openai(messages, max_tokens=512)
        return validation