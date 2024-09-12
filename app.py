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
        stream = client.chat.completions.create(
            model="o1-preview",  # Using the correct model name
            messages=conversation_history + [{"role": "user", "content": message.content}],
            stream=True,
        )

        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                await response_message.stream_token(chunk.choices[0].delta.content)

        # Update the message with the full content
        await response_message.update()

        # Save the user's message and the AI's response only after successful completion
        save_message("user", message.content)
        save_message("assistant", full_response)

    except Exception as e:
        # Handle any errors that occur during the API call or message sending
        error_message = f"An error occurred: {str(e)}"
        await cl.Message(content=error_message).send()

if __name__ == "__main__":
    cl.run()