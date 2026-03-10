import pystray
from PIL import Image
import threading
import gui

def create_image():
    img = Image.new("RGB", (64, 64), color=(0, 120, 255))
    return img

def show_window(icon, item):
    gui.show_gui()

def exit_app(icon, item):
    icon.stop()

def start_tray():

    icon = pystray.Icon(
        "ZYRA",
        create_image(),
        "ZYRA AI",
        menu=pystray.Menu(
            pystray.MenuItem("Open ZYRA", show_window),
            pystray.MenuItem("Exit", exit_app)
        )
    )

    icon.run()