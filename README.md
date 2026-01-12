# Gemini Chat Client (Python)

A simple Python script that demonstrates how to generate AI chat responses using the OpenAI client configured with Google’s Gemini API. The project showcases system role customization, response temperature control, and token limiting for cost-efficient AI conversations.

---

## Features

- Uses OpenAI Python client with Gemini backend
- Supports system and user role messages
- Adjustable creativity via temperature parameter
- Token usage control to prevent overspending
- Environment variable–based API key security
- Terminal-based output

---

## How It Works

1. Loads the API key from an environment variable
2. Initializes the OpenAI client with Gemini’s API endpoint
3. Sends system and user messages to the model
4. Receives a generated response from the AI
5. Prints the reply to the terminal

---

## Requirements

- Python 3.8+
- OpenAI Python SDK

```bash
pip install openai
