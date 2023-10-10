# voice-controlled-AI-assistant
This Python script creates an AI assistant that listens to voice commands, processes them using OpenAI's GPT-3.5 for natural language understanding and generation, and provides text-based responses. 

### Requirements 
OpenAI API key (set in the api_key variable)
Python libraries: openai, playsound, gtts, speech_recognition

### Setting Up Libraries in a Virtual Environment
To run this code in your own virtual environment, you'll need to set up the necessary Python libraries. Here's a step-by-step guide on how to do that

### Create a Virtual Environment (Optional but Recommended)
You can create a virtual environment to isolate your project dependencies. This step is optional but recommended for managing library versions and avoiding conflicts with other Python projects.


```shell
# Create a virtual environment (replace 'my_env' with your preferred name)
python -m venv my_env

# Activate the virtual environment
source my_env/bin/activate  # On Linux/macOS
# OR
my_env\Scripts\activate    # On Windows
```
Once your virtual environment is active, you can install the required libraries using pip. Make sure you have the latest version of pip installed.

### Install Required Libraries

```shell
pip install openai
pip install playsound
pip install gtts
pip install SpeechRecognition
```
This will install the OpenAI library, Playsound for audio playback, gTTS for text-to-speech, and SpeechRecognition for voice recognition.

### API Key Setup
Set up your OpenAI API key by editing the api_key variable in your Python script with your actual API key
```python
api_key = 'your_api_key_here'
```
you can get your API key by signing up for OpenAI's services on their website ```https://openai.com/```
