from utils import colored_text
import subprocess

def run(args):
    if len(args) < 2:
        print(colored_text("Usage: pkg install <package>", "yellow"))
        return

    if args[1] == "install" and len(args) >= 3:
        package = args[2]
        print(colored_text(f"Installing {package} via apt...", "cyan"))
        try:
            subprocess.run(f"apt install {package} -y", shell=True)
        except Exception as e:
            print(colored_text(f"Install failed: {e}", "red"))
    else:
        print(colored_text("Unknown pkg command", "red"))
