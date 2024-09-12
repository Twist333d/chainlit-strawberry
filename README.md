# Chainlit Strawberry 🍓

This project is a chatbot application that uses OpenAI's latest model, o1-preview, to generate responses. It's built with Chainlit, providing a seamless chat interface for interacting with the AI.

## Features

- Utilizes OpenAI's o1-preview model for state-of-the-art language processing
- Implements a conversational memory to maintain context throughout the chat
- Built with Chainlit for an intuitive and responsive chat interface
- Handles API errors gracefully

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

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
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

This will start the Chainlit server, and you can access the chat interface by opening a web browser and navigating to `http://localhost:8000`.

## Configuration

You can modify the `app.py` file to change the behavior of the chatbot. Key areas you might want to adjust include:

- The model name (currently set to "o1-preview")
- The system message or initial prompt
- The conversation history management

## Contributing

Contributions to the Chainlit Strawberry project are welcome. Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- OpenAI for providing the o1-preview model
- Chainlit for the excellent chat interface framework

## Contact

If you have any questions or feedback, please open an issue on the GitHub repository.

Enjoy chatting with the latest AI technology! 🍓🤖
