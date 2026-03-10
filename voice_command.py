import speech_recognition as sr

def listen_command():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for command...")

        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("User said:", command)

        return command.lower()

    except:
        print("Sorry, could not understand")
        return ""