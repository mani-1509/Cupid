from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY")
)

# Initial question
INITIAL_QUESTION = "What makes you feel most loved? For example, do you appreciate gifts, quality time, or words of affirmation?"

@app.route("/")
def home():
    return render_template("quiz.html", question=INITIAL_QUESTION)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    conversation = request.json.get("conversation", [])

    # Add user's message to the conversation
    conversation.append({"role": "user", "content": user_input})

    # Get AI response
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct",
        temperature=0.7,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that helps users discover their love language. Ask thoughtful questions and provide suggestions based on their responses. Format your responses in Markdown."},
            *conversation
        ]
    )

    # Extract AI response
    ai_message = response.choices[0].message.content.strip()

    # Add AI's message to the conversation
    conversation.append({"role": "assistant", "content": ai_message})

    return jsonify({
        "response": ai_message,
        "conversation": conversation
    })

if __name__ == "__main__":
    app.run(debug=True)