import webbrowser

def open_youtube():

    webbrowser.open("https://youtube.com")

def open_chatgpt():

    webbrowser.open("https://chat.openai.com")

def google_search(query):

    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)