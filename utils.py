import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def colored_text(text, color):
    colors = {
        "black": "\033[30m", "red": "\033[31m", "green": "\033[32m",
        "yellow": "\033[33m", "blue": "\033[34m", "magenta": "\033[35m",
        "cyan": "\033[36m", "white": "\033[37m", "reset": "\033[0m"
    }
    return f"{colors.get(color, colors['white'])}{text}{colors['reset']}"
