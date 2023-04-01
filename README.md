# ChatGenie Telegram Bot

## Introduction
ChatGenie is an AI-powered Telegram bot built using Python and the aiogram library. 
It uses the OpenAI ChatGPT API to generate responses to user messages in natural language. 
ChatGenie can be used to chat with users, answer questions, and provide recommendations or suggestions.

## Prerequisites

- python3
- venv
- aiogram

## Installation
1. Clone the repository using Git:
`git clone git@github.com:victoriademina/ChatGenie.git`
2. Navigate to the project directory:
`cd ChatGenie`
3. Create a virtual environment for the project:
`python3 -m venv venv`
4. Activate the virtual environment:
`source venv/bin/activate`
5. Install the required Python packages using pip:
`pip3 install -r requirements.txt`
6. Set up the environment variables for the Telegram bot token and the OpenAI API key:
```
export API_TOKEN=<your-telegram-bot-token>
export OPENAI_API_KEY=<your-openai-api-key>
```
7. Run the bot using the `python3 main.py` command.

## Usage
To use ChatGenie, simply add the bot to your Telegram account and start chatting with it. 
You can send any message or question to the bot, and it will generate a response using the ChatGPT API.

## License
This project is licensed under the MIT License. 
See the `LICENSE` file for details.

## Acknowledgements
This project was built using the following libraries and APIs:

- aiogram (https://github.com/aiogram/aiogram)
- OpenAI (https://openai.com/)
