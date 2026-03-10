import pyautogui
import time


def open_app(app_name):

    try:

        # Windows search open
        pyautogui.press("win")

        time.sleep(1)

        # app name type
        pyautogui.write(app_name)

        time.sleep(1)

        # open first result
        pyautogui.press("enter")

    except Exception as e:

        print("Error opening app:", e)