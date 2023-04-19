import openai


class ChatGPTManager:
    """ChatGPTManager"""
    def __init__(self):
        openai.api_key = "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"
        self.model = "gpt-3.5-turbo"

    def text_completion(self, system_prompt, user_prompt):
        """text_completion"""
        completion = openai.ChatCompletion.create(
            model=self.model,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        response = completion.choices[0].message.content
        return response

