from .agent_base import AgentBase

class RefinerAgent(AgentBase):
    def __init__(self, max_retries, verbose=True):
        super().__init__(name="RefinerAgent", max_retries=max_retries, verbose=verbose)

    def execute(self, draft):
        messages = [
            {"role": "system", 
             
             "content": [
                {
                    "type":"text",
                    "text":"You are an expert editor who refines and enhances articles for clarity, coherence and acdemic quality."
                }
             ]
             },
            {
                "role":"user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Please refine the following article draft to improve its language, coherence and overall quality:\n\n"
                            f"{draft}\n\n RefinedArticle:"
                        )
                    }

                ]
            }
        ] 
        refined_article = self.call_openai(messages, max_tokens=1000)
        return refined_article
    