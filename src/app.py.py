import gradio as gr
import openai
import config
from google.cloud import texttospeech
from google.oauth2 import service_account

# Initialize OpenAI and Google Cloud credentials
openai.api_key = config.api_key
credentials = service_account.Credentials.from_service_account_file('APP/annular-axe-417113-93a066605571.json')

# Global conversation history
conversation = []

def init_conversation():
    """
    Initializes the conversation with a system prompt.
    This sets the context for the 911 dispatcher scenario.
    """
    prompt = "You are a 911 dispatcher responsible for handling emergency calls. Your task is to quickly determine the nature of the emergency and gather essential information."
    conversation.append({"role": "system", "content": prompt})

def transcribe(audio_path):
    """
    Transcribes audio from the given file path using OpenAI's Whisper model.

    Args:
        audio_path (str): Path to the audio file to be transcribed.

    Returns:
        str: The transcribed text.
    """
    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            file=audio_file,
            model="whisper-1",
            response_format="text",
            language="en"
        )
    conversation.append({"role": "system", "content": transcript})
    return transcript

def get_system_response():
    """
    Generates a system response using the OpenAI ChatCompletion API,
    based on the conversation history.

    Returns:
        str: The system's message.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    system_message = response['choices'][0]['message']['content']
    conversation.append({"role": "system", "content": system_message})
    return system_message

def synthesize_speech(text):
    """
    Converts the given text into speech using Google's Text-to-Speech API.

    Args:
        text (str): The text to be converted into speech.

    Returns:
        str: The file path to the synthesized speech audio file.
    """
    client = texttospeech.TextToSpeechClient(credentials=credentials)
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

    output_file = "output.mp3"
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f'Audio content written to file "{output_file}"')

    return output_file

def process_audio(audio_path):
    """
    Orchestrates the full process: initializing the conversation, transcribing the audio,
    generating a system response, and converting that response to speech.

    Args:
        audio_path (str): Path to the input audio file.

    Returns:
        str: The file path to the synthesized response audio file.
    """
    init_conversation()
    transcribe(audio_path)
    system_message = get_system_response()
    return synthesize_speech(system_message)

def setup_gradio():
    """
    Sets up the Gradio interface for the audio processing application.

    Returns:
        gr.Interface: The Gradio interface object.
    """
    voice_interface = gr.Interface(
        fn=process_audio,
        inputs=gr.Audio(sources="microphone", type="filepath"),
        outputs=[gr.Audio(label="Response Audio")]
    )
    return voice_interface

# Main function to launch the Gradio interface
if __name__ == "__main__":
    interface = setup_gradio()
    interface.launch()
