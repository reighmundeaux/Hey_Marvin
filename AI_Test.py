# Import necessary libraries
import openai
import speech_recognition as sr
import pyttsx3

# Assign OpenAI API key
openai.api_key = "ENTER YOUR OPEN-AI API KEY"


# Initialize text-to-speech engine
engine = pyttsx3.init()


# Loop to listen for audio input
while True:
    
    
    
    # Create speech recognizer object
    r = sr.Recognizer()

    # Listen for input
    with sr.Microphone() as source:
        print(' _   _  _______   __          ___  ___  ___   ______   _   _  _____   _   _ ')
        print('| | | ||  ___\ \ / /          |  \/  | / _ \  | ___ \ | | | ||_   _| | \ | |')
        print('| |_| || |__  \ V /   ______  | .  . |/ /_\ \ | |_/ / | | | |  | |   |  \| |')
        print('|  _  ||  __|  \ /   |______| | |\/| ||  _  | |    /  | | | |  | |   | . ` |')
        print('| | | || |___  | |            | |  | || | | | | |\ \  \ \_/ / _| |_  | |\  |')
        print('\_| |_/\____/  \_/            \_|  |_/\_| |_/ \_| \_|  \___/  \___/  \_| \_/')
        
        print("What do you want")
        audio = r.listen(source)

    # Try to recognize the audio
    try:
        prompt = r.recognize_google(audio, language="en-EN", show_all=False)
        print("You asked:", prompt)

        # Use OpenAI to create a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=300
        )

        # Get the response text
        response_text = str(response['choices'][0]['text']).strip('\n\n')
        print(response_text)

        # Speak the response
        engine.say(response_text)
        engine.runAndWait()
        print()

    # Catch if recognition fails
    except:
        response_text = "Try again stupid"
        print(response_text)
        engine.say(response_text)
        engine.runAndWait()
        print()