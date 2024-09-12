import os
from openai import OpenAI
import chainlit as cl
from dotenv import load_dotenv

# Initialize env variables
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Global variable to store conversation history
conversation_history = []

def save_message(role, content):
    """Save a message to the conversation history."""
    conversation_history.append({"role": role, "content": content})

@cl.on_chat_start
async def start():
    await cl.Message(content="**Was the hype worth it?** 🍓🍓🍓").send()

@cl.on_message
async def main(message: cl.Message):
    try:
        # Create a new message and start sending it
        response_message = cl.Message(content="")
        await response_message.send()

        # Call OpenAI API
        response = client.chat.completions.create(
            model="o1-preview",  # Using the correct model name
            messages=conversation_history + [{"role": "user", "content": message.content}],
            stream=False,
        )

        # Extract the response content
        ai_response = response.choices[0].message.content

        # Add AI response to conversation history
        conversation_history.append({"role": "assistant", "content": ai_response})

        # Send the response
        await cl.Message(content=ai_response).send()
    except Exception as e:
        # Handle any errors that occur during the API call or message sending
        error_message = f"An error occurred: {str(e)}"
        await cl.Message(content=error_message).send()

if __name__ == "__main__":
    cl.run()