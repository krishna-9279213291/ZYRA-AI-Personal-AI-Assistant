import os

def shutdown_pc():
    os.system("shutdown /s /t 5")

def restart_pc():
    os.system("shutdown /r /t 5")

def open_settings():
    os.system("start ms-settings:")