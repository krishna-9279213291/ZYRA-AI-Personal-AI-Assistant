from automation.windows_search import open_app

from commands.browser_commands import open_youtube, open_chatgpt
from commands.whatsapp_commands import (
    send_whatsapp_message,
    open_whatsapp,
    voice_call,
    video_call,
    send_file,
    send_photo
)

from vision.vision_executor import read_my_screen, click_button


def execute_command(command):

    command = command.lower().strip()

    # -------------------------
    # Browser commands
    # -------------------------

    if "open youtube" in command:

        open_youtube()
        return "Opening YouTube..."

    elif "open chatgpt" in command:

        open_chatgpt()
        return "Opening ChatGPT..."

    # -------------------------
    # WhatsApp commands
    # -------------------------

    elif "open whatsapp" in command:

        open_whatsapp()
        return "Opening WhatsApp..."

    # SEND MESSAGE
    elif "whatsapp" in command and "message" in command:

        try:

            parts = command.split("to", 1)[1].strip()

            split_parts = parts.split(" ", 1)

            name = split_parts[0]

            message = ""

            if len(split_parts) > 1:
                message = split_parts[1]

            send_whatsapp_message(name, message)

            return f"Sending WhatsApp message to {name}"

        except Exception as e:

            print("WhatsApp message error:", e)

            return "Could not send WhatsApp message"

    # VOICE CALL
    elif "call" in command and "whatsapp" in command and "video" not in command:

        try:

            name = command.replace("call", "").replace("on whatsapp", "").strip()

            voice_call(name)

            return f"Calling {name} on WhatsApp"

        except Exception as e:

            print("Call error:", e)

            return "Could not start call"

    # VIDEO CALL
    elif "video call" in command:

        try:

            name = command.replace("video call", "").replace("on whatsapp", "").strip()

            video_call(name)

            return f"Starting video call with {name}"

        except Exception as e:

            print("Video call error:", e)

            return "Could not start video call"

    # SEND FILE
    elif "send file" in command:

        try:

            name = command.split("to")[1].strip()

            filepath = "C:/Users/Public/Documents/test.pdf"

            send_file(name, filepath)

            return f"Sending file to {name}"

        except:

            return "Could not send file"

    # SEND PHOTO
    elif "send photo" in command:

        try:

            name = command.split("to")[1].strip()

            photo_path = "C:/Users/Public/Pictures/test.jpg"

            send_photo(name, photo_path)

            return f"Sending photo to {name}"

        except:

            return "Could not send photo"

    # -------------------------
    # Vision Automation
    # -------------------------

    elif "read screen" in command:

        read_my_screen()
        return "Reading screen..."

    elif command.startswith("click "):

        button = command.replace("click ", "").strip()

        click_button(button)

        return f"Trying to click '{button}' button..."

    # -------------------------
    # Dynamic app open
    # -------------------------

    elif command.startswith("open "):

        app = command.replace("open ", "").strip()

        open_app(app)

        return f"Opening {app}..."

    return "No automation found"