import speech_recognition as sr
import pyttsx3
import threading

# ============================================
# SPEECH ENGINE SETUP
# ============================================

engine = pyttsx3.init()

engine.setProperty("rate", 170)      # speaking speed
engine.setProperty("volume", 1.0)    # volume

voices = engine.getProperty("voices")

# female voice (optional)
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)


# ============================================
# THREAD LOCK
# ============================================

speak_lock = threading.Lock()


# ============================================
# SPEAK FUNCTION
# ============================================

def speak(text):

    def run():

        with speak_lock:

            print("ZYRA:", text)

            engine.say(text)

            engine.runAndWait()

    threading.Thread(target=run, daemon=True).start()


# ============================================
# LISTEN FUNCTION
# ============================================

def listen():

    recognizer = sr.Recognizer()

    recognizer.pause_threshold = 1

    recognizer.energy_threshold = 300

    with sr.Microphone() as source:

        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except:

            return None

    try:

        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text.lower()

    except sr.UnknownValueError:

        print("Could not understand")

        return None

    except sr.RequestError:

        print("Speech service error")

        return None