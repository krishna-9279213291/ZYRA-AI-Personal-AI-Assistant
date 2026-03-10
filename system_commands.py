import os
from automation.windows_search import open_app

def open_chrome():

    open_app("chrome")

def open_notepad():

    open_app("notepad")

def open_file_explorer():

    os.system("explorer")

def shutdown_pc():

    os.system("shutdown /s /t 5")