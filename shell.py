import subprocess
import os
import readline
from utils import colored_text, clear_screen
import commands

class PyMUXShell:
    def __init__(self):
        self.running = True
        self.prompt = colored_text("pymux@termux $ ", "cyan")
        self.builtins = {
            "exit": self.exit_shell,
            "clear": clear_screen,
            "termux-open": commands.termux_open.run,
            "termux-info": commands.termux_info.run,
            "pkg": commands.pkg.run,
        }

    def run(self):
        clear_screen()
        print(colored_text("🚀 PyMUX Terminal Emulator v2.0", "green"))
        print("Type 'exit' to quit, 'clear' to clear the screen.\n")

        while self.running:
            try:
                command = input(self.prompt).strip()
                if not command:
                    continue

                cmd_parts = command.split()
                base_cmd = cmd_parts[0]

                if base_cmd in self.builtins:
                    self.builtins[base_cmd](cmd_parts)
                else:
                    self.execute(command)

            except KeyboardInterrupt:
                print(colored_text("\n[!] Ctrl+C caught. Use 'exit' to quit.", "red"))
            except Exception as e:
                print(colored_text(f"[Error] {e}", "red"))

    def execute(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.stdout:
                print(colored_text(result.stdout, "white"))
            if result.stderr:
                print(colored_text(result.stderr, "red"))
        except Exception as e:
            print(colored_text(f"[Execution Error] {e}", "red"))

    def exit_shell(self, *args):
        self.running = False
        print(colored_text("👋 Exiting PyMUX Terminal...", "yellow"))
