import pytesseract
import pyautogui
import cv2
import numpy as np

# tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def read_screen():

    screenshot = pyautogui.screenshot()

    img = np.array(screenshot)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(img)

    return text