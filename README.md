# Audio-Based Emergency Response Assistant

## Overview
This project provides a novel approach to handling emergency calls through an audio-based interface. Utilizing advanced AI technologies, including OpenAI's Whisper model for transcription and GPT-3.5-turbo for generating responses, alongside Google Cloud's Text-to-Speech for voice synthesis, it simulates a 911 dispatcher scenario. This system is designed to quickly determine the nature of emergencies and gather essential information through an intuitive audio conversation.

## Features
- Audio transcription using OpenAI's Whisper model.
- Response generation with OpenAI's GPT models.
- Speech synthesis via Google Cloud's Text-to-Speech API.
- Gradio interface for easy interaction.

## Function Descriptions
- init_conversation(): Initializes the conversation context for the emergency scenario.
- transcribe(audio_path): Transcribe the provided audio file to text.
- get_system_response(): Generates a response based on the conversation history.
- synthesize_speech(text): Converts text to speech.
- process_audio(audio_path): Orchestrates the full process from audio transcription to response synthesis.
- setup_gradio(): Sets up the Gradio interface.

## Diagram
Here is the flow of the application:
![Green and White Project Phases Flowchart (1)](https://github.com/NimaHagh/AIEmergencyResponder/assets/105126750/b7da17ad-e179-4f13-b11b-a2f49d9b5133)


## Prerequisites
Before you start, ensure you have the following:

- Python 3.7 or later.
- Gradio, OpenAI, and Google Cloud libraries installed.
- An OpenAI API key.
- A Google Cloud account with Text-to-Speech API enabled and a service account created.

## Installation
1- Clone the repository to your local machine:
```
git clone https://github.com/NimaHagh/AIEmergencyResponder.git
```
2- Install required Python packages:
```
pip install -r requirements.txt
```
3- Set up your config.py file with your OpenAI API key: (or set up .env)
```
api_key = "your_openai_api_key_here"
``` 
