import speech_recognition as sr

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise for better recognition
        recognizer.adjust_for_ambient_noise(source)

        # Listen for speech input
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")

        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)

        print("You said:", text)

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Error occurred: {0}".format(e))

if __name__ == '__main__':
    recognize_speech()





