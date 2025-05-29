from utils import colored_text
import webbrowser

def run(args):
    if len(args) < 2:
        print(colored_text("Usage: termux-open <url>", "yellow"))
        return
    url = args[1]
    print(colored_text(f"Opening {url} in browser...", "green"))
    webbrowser.open(url)
