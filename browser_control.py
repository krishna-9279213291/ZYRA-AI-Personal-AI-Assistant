import webbrowser

def open_google():
    webbrowser.open("https://google.com")

def open_youtube():
    webbrowser.open("https://youtube.com")

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)