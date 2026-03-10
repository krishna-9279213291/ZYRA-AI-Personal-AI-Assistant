import tkinter as tk
import threading

import voice
import memory
from assistant import process_command


data = memory.load_memory()


# -------- MEMORY --------
def process_memory(user):

    user = user.lower()

    if "my name is" in user:

        name = user.split("is")[-1].strip()

        data["name"] = name

        memory.save_memory(data)

        return f"Nice to meet you {name}"

    if "what is my name" in user:

        name = data.get("name")

        if name:
            return f"Your name is {name}"

    return None


# -------- SCROLL --------
def scroll_to_bottom():

    canvas.update_idletasks()

    canvas.yview_moveto(1.0)


# -------- USER MESSAGE --------
def add_user_message(text):

    frame = tk.Frame(chat_frame, bg="#121212")

    bubble = tk.Label(
        frame,
        text=text,
        bg="#2962ff",
        fg="white",
        wraplength=450,
        justify="left",
        padx=14,
        pady=8,
        font=("Segoe UI", 10)
    )

    bubble.pack(anchor="e")

    frame.pack(fill="x", pady=6, padx=10)

    scroll_to_bottom()


# -------- AI MESSAGE --------
def add_ai_message(text):

    frame = tk.Frame(chat_frame, bg="#121212")

    bubble = tk.Label(
        frame,
        text=text,
        bg="#00c853",
        fg="black",
        wraplength=450,
        justify="left",
        padx=14,
        pady=8,
        font=("Segoe UI", 10)
    )

    bubble.pack(anchor="w")

    frame.pack(fill="x", pady=6, padx=10)

    voice.speak(text)

    scroll_to_bottom()


# -------- TYPING INDICATOR --------
typing_label = None


def show_typing():

    global typing_label

    typing_label = tk.Label(
        chat_frame,
        text="ZYRA is thinking...",
        fg="gray",
        bg="#121212",
        font=("Segoe UI", 9, "italic")
    )

    typing_label.pack(anchor="w", padx=10)

    scroll_to_bottom()


def hide_typing():

    global typing_label

    if typing_label:

        typing_label.destroy()

        typing_label = None


# -------- AI RESPONSE --------
def get_ai_response(user):

    root.after(0, show_typing)

    response = process_command(user)

    root.after(0, hide_typing)

    root.after(0, lambda: add_ai_message(response))


# -------- SEND MESSAGE --------
def send_message(event=None):

    user = entry.get().strip()

    if not user:
        return

    add_user_message(user)

    entry.delete(0, tk.END)

    mem = process_memory(user)

    if mem:

        add_ai_message(mem)

        return

    threading.Thread(
        target=get_ai_response,
        args=(user,),
        daemon=True
    ).start()


# -------- VOICE COMMAND --------
def voice_command():

    user = voice.listen()

    if not user:
        return

    add_user_message(user)

    mem = process_memory(user)

    if mem:

        add_ai_message(mem)

        return

    threading.Thread(
        target=get_ai_response,
        args=(user,),
        daemon=True
    ).start()


# -------- GUI --------
root = tk.Tk()

root.title("ZYRA AI")

root.geometry("520x640")

root.configure(bg="#121212")


# -------- HEADER --------
header = tk.Frame(root, bg="#0f172a", height=55)

header.pack(fill="x")

title = tk.Label(
    header,
    text="⚡ ZYRA AI Assistant",
    bg="#0f172a",
    fg="#00e5ff",
    font=("Segoe UI", 15, "bold")
)

title.pack(pady=12)


# -------- CHAT AREA --------
chat_container = tk.Frame(root, bg="#121212")

chat_container.pack(fill="both", expand=True)

canvas = tk.Canvas(chat_container, bg="#121212", highlightthickness=0)

scrollbar = tk.Scrollbar(
    chat_container,
    orient="vertical",
    command=canvas.yview
)

scrollbar.pack(side="right", fill="y")

canvas.pack(side="left", fill="both", expand=True)

canvas.configure(yscrollcommand=scrollbar.set)

chat_frame = tk.Frame(canvas, bg="#121212")

canvas_window = canvas.create_window((0, 0), window=chat_frame, anchor="nw")


def on_configure(event):

    canvas.configure(scrollregion=canvas.bbox("all"))


chat_frame.bind("<Configure>", on_configure)


# -------- FIX WIDTH --------
def resize_chat(event):

    canvas.itemconfig(canvas_window, width=event.width)


canvas.bind("<Configure>", resize_chat)


# -------- MOUSE SCROLL --------
def mouse_scroll(event):

    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


canvas.bind_all("<MouseWheel>", mouse_scroll)


# -------- INPUT --------
input_frame = tk.Frame(root, bg="#1f2937")

input_frame.pack(fill="x")

entry = tk.Entry(
    input_frame,
    font=("Segoe UI", 11),
    bg="#374151",
    fg="white",
    insertbackground="white",
    relief="flat"
)

entry.pack(side="left", fill="x", expand=True, padx=8, pady=10)

entry.bind("<Return>", send_message)


send_btn = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    bg="#00bcd4",
    fg="black",
    relief="flat",
    padx=16
)

send_btn.pack(side="right", padx=6)


voice_btn = tk.Button(
    input_frame,
    text="🎤",
    command=lambda: threading.Thread(target=voice_command).start(),
    bg="#4b5563",
    fg="white",
    relief="flat",
    padx=12
)

voice_btn.pack(side="right")


# -------- GUI CONTROL --------
def show_gui():
    root.deiconify()


def hide_gui():
    root.withdraw()


root.withdraw()


def start_gui():
    root.mainloop()