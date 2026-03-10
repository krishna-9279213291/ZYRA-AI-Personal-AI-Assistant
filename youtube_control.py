import webbrowser

def play_video(name):

    url = f"https://www.youtube.com/results?search_query={name}"

    webbrowser.open(url)