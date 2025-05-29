from utils import colored_text
import platform
import os

def run(args):
    print(colored_text("📱 PyMUX System Info", "blue"))
    print(f"OS      : {platform.system()} {platform.release()}")
    print(f"Machine : {platform.machine()}")
    print(f"Python  : {platform.python_version()}")
    print(f"User    : {os.getenv('USER') or os.getenv('USERNAME')}")
