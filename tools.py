import os
import webbrowser
import pyautogui
import time
from automation.windows_search import open_app
from commands.whatsapp_commands import send_whatsapp_message 

# ---------- WINDOWS SEARCH APP OPEN ----------

def open_app(app_name):

    pyautogui.press("win")
    time.sleep(1)

    pyautogui.write(app_name)
    time.sleep(1)

    pyautogui.press("enter")

    time.sleep(2)


# ---------- MAIN COMMAND FUNCTION ----------

def run_command(user):

    user = user.lower()


    # OPEN CHROME
    if "open chrome" in user:

        open_app("chrome")
        return "Opening Chrome"


    # OPEN NOTEPAD
    if "open notepad" in user:

        open_app("notepad")
        return "Opening Notepad"


    # OPEN VS CODE
    if "open vs code" in user or "open vscode" in user:

        open_app("visual studio code")
        return "Opening VS Code"


    # OPEN CALCULATOR
    if "open calculator" in user:

        open_app("calculator")
        return "Opening Calculator"


    # OPEN FILE EXPLORER
    if "open file explorer" in user:

        os.system("explorer")
        return "Opening File Explorer"


    # OPEN YOUTUBE
    if "open youtube" in user:

        webbrowser.open("https://youtube.com")
        return "Opening YouTube"


    # OPEN CHATGPT
    if "open chatgpt" in user:

        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT"


    # OPEN WHATSAPP
    if "open whatsapp" in user:

        open_app("whatsapp")
        return "Opening WhatsApp"


    # GOOGLE SEARCH
    if "search" in user:

        query = user.replace("search", "").strip()

        url = "https://www.google.com/search?q=" + query

        webbrowser.open(url)

        return "Searching Google for " + query


    # YOUTUBE SEARCH
    if "play" in user:

        song = user.replace("play", "").strip()

        url = "https://www.youtube.com/results?search_query=" + song

        webbrowser.open(url)

        return "Playing " + song + " on YouTube"


    # SHUTDOWN PC
    if "shutdown pc" in user:

        os.system("shutdown /s /t 5")
        return "Shutting down the computer"


    # RESTART PC
    if "restart pc" in user:

        os.system("shutdown /r /t 5")
        return "Restarting the computer"


    # OPEN ANY APP (fallback)
    if "open" in user:

        app = user.replace("open", "").strip()

        open_app(app)

        return "Opening " + app


    return None