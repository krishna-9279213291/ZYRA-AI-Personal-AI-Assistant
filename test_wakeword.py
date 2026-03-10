import pvporcupine
import pyaudio
import struct
import speech_recognition as sr
import os

# 🔑 Picovoice Access Key
ACCESS_KEY = "gB5ypxJnURkfuM1FRZFTyW4UZuGV6SNEYNFomDTLr+JyOEssntq0RA=="

# Wake word engine
porcupine = pvporcupine.create(
    access_key=ACCESS_KEY,
    keywords=["jarvis"]
)

# Mic setup
pa = pyaudio.PyAudio()

stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

# Speech recognizer
recognizer = sr.Recognizer()

print("🎤 Listening for wake word...")

while True:

    pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

    keyword_index = porcupine.process(pcm)

    if keyword_index >= 0:

        print("🔥 Wake word detected!")

        with sr.Microphone() as source:

            print("🎧 Listening for command...")

            audio = recognizer.listen(source)

        try:

            command = recognizer.recognize_google(audio)
            command = command.lower()

            print("🗣 User said:", command)

            # 🧠 Command Logic

            if "chrome" in command:
                print("🌐 Opening Chrome...")
                os.system("start chrome")

            elif "youtube" in command:
                print("▶ Opening YouTube...")
                os.system("start https://www.youtube.com")

            elif "google" in command:
                print("🔎 Opening Google...")
                os.system("start https://www.google.com")

            else:
                print("❌ Command not recognized")

        except:
            print("⚠ Could not understand command")