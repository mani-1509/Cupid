from openai import OpenAI
import os


class LangMacher:
    # Initial question
    INITIAL_QUESTION = "What makes you feel most loved? For example, do you appreciate gifts, quality time, or words of affirmation?"
    
    def __init__(self):
        self.client = OpenAI(
            base_url="https://api.studio.nebius.ai/v1/",
            api_key=os.getenv("NEBIUS_API_KEY"),
        )

    def chat(self, message, conversation):
        """Send a message to the chat model and return the response."""
        conversation.append({"role": "user", "content": message})
        response = self.client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct",
            temperature=0.7,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that helps users discover their love language. Ask thoughtful questions and provide suggestions based on their responses. Format your responses in Markdown."},
                *conversation
            ]
        )
        ai_message = response.choices[0].message.content.strip()
        conversation.append({"role": "assistant", "content": ai_message})
        return ai_message, conversation