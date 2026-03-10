from vision.vision_reader import read_screen
from vision.element_clicker import click_text


def read_my_screen():

    text = read_screen()

    print("\n--- Screen Text ---\n")
    print(text)
    print("\n-------------------\n")


def click_button(name):

    result = click_text(name)

    if result:
        print(f"Clicked: {name}")

    else:
        print(f"Button not found: {name}")