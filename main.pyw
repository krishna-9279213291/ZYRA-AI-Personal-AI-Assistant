import threading
import wakeword
import gui
import sys

print("ZYRA AI Starting...")

if len(sys.argv) > 1 and sys.argv[1] == "manual":

    print("Manual mode")

    gui.show_gui()
    gui.start_gui()

else:

    print("Background mode")

    threading.Thread(target=wakeword.start_listening, daemon=True).start()

    gui.start_gui()