import pytesseract
import pyautogui
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def click_text(target):

    screenshot = pyautogui.screenshot()

    img = np.array(screenshot)

    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

    for i, text in enumerate(data["text"]):

        if target.lower() in text.lower():

            x = data["left"][i]
            y = data["top"][i]
            w = data["width"][i]
            h = data["height"][i]

            center_x = x + w // 2
            center_y = y + h // 2

            pyautogui.click(center_x, center_y)

            return True

    return False