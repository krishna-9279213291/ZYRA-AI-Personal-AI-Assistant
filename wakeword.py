import pvporcupine
import pyaudio
import struct
import voice
import gui
import brain
import memory

from utils.command_router import execute_command


ACCESS_KEY = "gB5ypxJnURkfuM1FRZFTyW4UZuGV6SNEYNFomDTLr+JyOEssntq0RA=="

porcupine = pvporcupine.create(
    access_key=ACCESS_KEY,
    keywords=["jarvis"]
)

pa = pyaudio.PyAudio()

stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)


def start_listening():

    print("Wake word listening...")

    while True:

        pcm = stream.read(
            porcupine.frame_length,
            exception_on_overflow=False
        )

        pcm = struct.unpack_from(
            "h" * porcupine.frame_length,
            pcm
        )

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:

            print("Wake word detected!")

            # GUI popup
            gui.show_gui()

            # voice command listen
            command = voice.listen()

            if command:

                print("User:", command)

                # RUN COMMAND ROUTER
                cmd = execute_command(command)

                if cmd:

                    gui.chat.insert(
                        "end",
                        "ZYRA: " + cmd + "\n\n"
                    )

                    voice.speak(cmd)

                else:

                    # AI fallback
                    ai = brain.ask_ai(command)

                    gui.chat.insert(
                        "end",
                        "ZYRA: " + ai + "\n\n"
                    )

                    voice.speak(ai)

            # GUI auto hide
            gui.root.after(10000, gui.hide_gui)