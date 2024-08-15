import telebot
import whisper
from moviepy.editor import AudioFileClip
import speech_recognition as sr
import google.generativeai as genai
from gtts import gTTS

# Initialize the bot and recognizer
bot = telebot.TeleBot("TELEGRAM-API", parse_mode=None)
r = sr.Recognizer()

# Configure Google Generative AI
def configure_genai():
    genai.configure(api_key="GEMINI-API")
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]
    model = genai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=generation_config,
        safety_settings=safety_settings
    )
    return model.start_chat(history=[])

convo = configure_genai()

# Process and save the voice message
def process_voice_message(message):
    voice_file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(voice_file_info.file_path)
    with open("voice_message.ogg", 'wb') as f:
        f.write(downloaded_file)
    convert_audio("voice_message.ogg")

# Convert .ogg to .wav
def convert_audio(ogg_file):
    audio_clip = AudioFileClip(ogg_file)
    audio_clip.write_audiofile("voice_message.wav")

# Transcribe audio to text
def transcribe_audio():
    audio = sr.AudioFile("voice_message.wav")
    with audio as source:
        audio_data = r.record(source)
        return r.recognize_google(audio_data)

# Generate AI response
def generate_ai_response(text):
    convo.send_message(text)
    return convo.last.text

# Convert text to speech and save as .ogg
def text_to_speech(response_text):
    tts = gTTS(response_text)
    tts.save('response.ogg')

# Handle incoming messages
@bot.message_handler(content_types=['text', 'audio', 'voice'])
def handle_message(message):
    if message.content_type == 'voice':
        bot.reply_to(message, "I've received a voice message! Please give me a second to respond :)")
        process_voice_message(message)
        transcribed_text = transcribe_audio()
        bot.reply_to(message, f"*You*: {transcribed_text}")
        ai_response = generate_ai_response(transcribed_text)
        text_to_speech(ai_response)
        send_voice_response(message.chat.id, 'response.ogg')
    else:
        bot.reply_to(message, "Sorry, I can only process voice messages at the moment.")

# Send voice response to the user
def send_voice_response(chat_id, voice_file):
    with open(voice_file, 'rb') as voice:
        bot.send_voice(chat_id, voice)

print('System online')
bot.infinity_polling()
