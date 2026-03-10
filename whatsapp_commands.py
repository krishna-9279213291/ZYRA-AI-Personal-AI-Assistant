import pyautogui
import time
import subprocess
import pyperclip


def open_whatsapp():

    print("Opening WhatsApp")

    subprocess.Popen("start whatsapp:", shell=True)

    time.sleep(7)

    pyautogui.click(500, 500)


def search_contact(name):

    print("Searching:", name)

    pyautogui.hotkey("ctrl", "f")

    time.sleep(1)

    pyautogui.write(name, interval=0.1)

    time.sleep(2)

    pyautogui.press("enter")

    time.sleep(2)


def send_whatsapp_message(name, message):

    open_whatsapp()

    search_contact(name)

    pyperclip.copy(message)

    pyautogui.hotkey("ctrl", "v")

    time.sleep(1)

    pyautogui.press("enter")

    print("Message sent")


def send_file(name, filepath):

    open_whatsapp()

    search_contact(name)

    pyautogui.hotkey("ctrl", "o")

    time.sleep(2)

    pyperclip.copy(filepath)

    pyautogui.hotkey("ctrl", "v")

    pyautogui.press("enter")

    time.sleep(2)

    pyautogui.press("enter")

    print("File sent")


def send_photo(name, photo_path):

    open_whatsapp()

    search_contact(name)

    pyautogui.hotkey("ctrl", "o")

    time.sleep(2)

    pyperclip.copy(photo_path)

    pyautogui.hotkey("ctrl", "v")

    pyautogui.press("enter")

    time.sleep(2)

    pyautogui.press("enter")

    print("Photo sent")


def voice_call(name):

    open_whatsapp()

    search_contact(name)

    time.sleep(2)

    # click call icon
    pyautogui.click(1670,110)

    time.sleep(2)

    # move to popup center
    screen_width, screen_height = pyautogui.size()

    x = screen_width // 2 - 120
    y = screen_height // 2 - 40

    pyautogui.click(x, y)

    print("Voice call started")

def video_call(name):

    open_whatsapp()

    search_contact(name)

    time.sleep(2)

    # click call icon
    pyautogui.click(1670,110)

    time.sleep(2)

    screen_width, screen_height = pyautogui.size()

    x = screen_width // 2 + 120
    y = screen_height // 2 - 40

    pyautogui.click(x, y)

    print("Video call started")