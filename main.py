'''
:Author: Edward Phiri
:Email: edwardphirijr698@gmail.com
:Date: 19/08/2023
:version: 1.0
:Public: [Yes]
'''
#import open AI module 
import openai
#import Play sound module 
from playsound import playsound
#import Google text to speech for module
from gtts import gTTS
#Import a module for speech recognition 
import speech_recognition
#import Oparating System to your desired OS which you are using 
import os
#Set your OpenAI API key here
api_key = ''
#Initialize the OpenAI API client
openai.api_key = api_key
#Initialize the speech synthesis
recognizer = speech_recognition.Recognizer()
while True:
    display = 'Listening!'
    #Wake word acive. It pops a sound then prompt you to enter your desired Quetion 
    #for playing note.mp3 file
    playsound('POP_sound.mp3')
    print(display)
    try:
           with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized {text}")
            if text == "ok":
                playsound('POP_sound.mp3')
                print("Done testing!!")
            #Input prompt to start the conversation
            #Text = input("Enter your prompt here: ")
            conversation = text
#Function to generate text using ChatGPT
            def generate_text(prompt, max_tokens=50):
                response = openai.Completion.create(
                engine="text-davinci-003",  # Choose the GPT-3.5 engine
                prompt=prompt,
                max_tokens=max_tokens
                )
                return response.choices[0].text.strip()
#Generate a continuation of the conversation
            response = generate_text(conversation, max_tokens=100)
            #It pops a sound then gives a user an Answer
            #for playing note.mp3 file
            playsound('Answer_Sound.mp3')
            #Print the generated response
            print("Response:", response)
            #Initialize the gTTS object
            tts = gTTS(text=response, lang='en')
            #Save the generated audio to a file the proceed to play thje save file in output
            #as an Audio file 
            tts.save("output.mp3")
            #for playing note.mp3 file
            playsound('output.mp3')
            #Play the generated audio
            os.system("output.mp3")
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue
    if text == " what's your name" or text ==  "what do you call yourself" or text == " What do you call yourself":
        print("I am Ostrich AI Assistant")

