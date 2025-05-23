import openai

class ChatEngine:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.history = []

    def ask(self, prompt):
        self.history.append({"role": "user", "content": prompt})

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=self.history
        )
        answer = response['choices'][0]['message']['content']
        self.history.append({"role": "assistant", "content": answer})

        return answer
