import openai
from playsound import playsound
from gtts import gTTS
import speech_recognition
import os
# Set your OpenAI API key here
api_key = ''
# Initialize the OpenAI API client
openai.api_key = api_key
# Initialize the speech recognition
recognizer = speech_recognition.Recognizer()
def generate_text(prompt, max_tokens=50):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()
while True:
    playsound('POP_sound.mp3')
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)  
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized {text}")
            conversation = text
            response = generate_text(conversation, max_tokens=100)
            playsound('Answer_Sound.mp3')
            print("Response:", response)
            # Initialize the gTTS object
            tts = gTTS(text=response, lang='en')
            tts.save("output.mp3")
            # Play the generated audio
            playsound('output.mp3')
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue
    if "name" in conversation.lower() or "call yourself" in conversation.lower():
        print("I am Ostrich AI Assistant")
