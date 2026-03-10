import pyautogui
import time

def type_text(text):

    pyautogui.write(text)
    time.sleep(1)

def press_enter():

    pyautogui.press("enter")

def click_position(x, y):

    pyautogui.click(x, y)

def hotkey(key1, key2):

    pyautogui.hotkey(key1, key2)