# AI-Voice-Chatbot-for-Telegram-using-Python

## Overview
This project is a Python-based Telegram bot designed to process and respond to voice messages. The bot listens for voice inputs, transcribes them to text using Google's Speech Recognition, generates intelligent responses using Google's Generative AI (Gemini 1.0), and replies with synthesized voice messages. It provides a seamless interaction experience by leveraging advanced AI and speech processing technologies.

## Features
- **Voice Message Handling**: Receives and processes voice messages from Telegram users.
- **Speech Recognition**: Converts voice messages to text using the `speech_recognition` library.
- **Generative AI Integration**: Generates context-aware and intelligent responses using Google's Generative AI model.
- **Text-to-Speech Conversion**: Converts the AI-generated text responses back into speech using Google Text-to-Speech (gTTS).
- **Telegram Integration**: Uses the `telebot` library to interact with users in real-time on Telegram.

## Installation

### Prerequisites
- Python 3.7 or later
- Telegram API Token (from BotFather)
- Google API Key (for Generative AI)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sandaruwan-Hewavitharana/AI-Voice-Chatbot-for-Telegram-using-Python.git
   cd AI-Voice-Chatbot-for-Telegram-using-Python

