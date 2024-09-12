# Chainlit Strawberry 🍓

Chat with `o1-preview` via API in Chainlit.

## Features

- Utilizes OpenAI's o1-preview model 
- Implements a conversational memory to maintain context throughout the chat
- Built with Chainlit 

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- An OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Twist333d/chainlit-strawberry.git
   cd chainlit-strawberry
   ```

2. Install the required dependencies using Poetry:
   ```
   poetry install
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

To run the chatbot, use the following command:

```
chainlit run app.py
```

Enjoy chatting with 🍓🤖!

