import pyautogui
import cv2
import numpy as np


def find_button(image_path, confidence=0.8):

    location = pyautogui.locateOnScreen(image_path, confidence=confidence)

    if location:

        center = pyautogui.center(location)

        pyautogui.click(center)

        return True

    return False