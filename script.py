import os
import subprocess
import platform
import sys
import configparser

# Define the default settings
DEFAULT_SETTINGS = """
[General]
elevated_mode = False
powershell_mode = False
"""

# Ensure settings.ini exists with default settings
def ensure_settings_file():
    if not os.path.isfile('settings.ini'):
        print("Settings file not found. Generating default settings.ini...")
        with open('settings.ini', 'w') as f:
            f.write(DEFAULT_SETTINGS)
        print("Default settings.ini created.")

# Load settings from settings.ini
def load_settings():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return {
        'elevated_mode': config.getboolean('General', 'elevated_mode', fallback=False),
        'powershell_mode': config.getboolean('General', 'powershell_mode', fallback=False)
    }

# Ensure settings file exists
ensure_settings_file()
settings = load_settings()

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_help_sim():
    print("""
Custom Commands:
- help_sim: Display this help message with details about custom commands.
- cd <directory>: Changes the current directory to <directory>. Use ".." to go up one level.
- run <arg>: Executes system control commands:
    - 'sh' or 'shutdown': Shuts down the system immediately.
    - 'r' or 'restart': Restarts the system immediately.
    - 'logoff': Logs off the current user.
    - 'h' or 'hibernate': Puts the system into hibernation mode.
- exit: Exits the command prompt simulator.
- clear: Clears the terminal screen.
    """)

def run_system_command(command):
    try:
        if settings['powershell_mode']:
            command = f"powershell -Command \"{command}\""

        if settings['elevated_mode'] and ("shutdown" in command or "reboot" in command):
            if platform.system() == "Windows":
                subprocess.run(["runas", "/user:Administrator", command], shell=True)
            else:
                subprocess.run(f"sudo {command}", shell=True)
        else:
            subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print(f"The system cannot find the path specified: {path}")
    except NotADirectoryError:
        print(f"Not a directory: {path}")
    except PermissionError:
        print(f"Permission denied: {path}")

def execute_command(command):
    command = command.strip()
    if not command:
        return

    if command.lower() == "exit":
        print("Exiting simulator...")
        sys.exit(0)
    elif command.lower() == "clear":
        clear_screen()
    elif command.lower() == "help":
        if platform.system() == "Windows":
            subprocess.run("help", shell=True)
        else:
            subprocess.run("man bash", shell=True)
    elif command.lower() == "help_sim":
        print_help_sim()
    elif command.lower().startswith("run"):
        args = command.split(maxsplit=1)
        if len(args) > 1:
            run_system_command(args[1])
        else:
            print("Usage: run <command>")
    elif command.lower().startswith("cd"):
        args = command.split(maxsplit=1)
        if len(args) > 1:
            change_directory(args[1])
        else:
            print("Usage: cd <directory>")
    else:
        run_system_command(command)

def print_powershell_prompt(current_directory):
    print(f"\033[94mPS {current_directory}> \033[0m", end='')

def main():
    print("Advanced Command Prompt Simulator. Type 'help_sim' for detailed help on custom commands.")
    
    while True:
        current_directory = os.getcwd()
        
        if settings['powershell_mode']:
            print_powershell_prompt(current_directory)
        
        prompt = f"{current_directory}> " if not settings['powershell_mode'] else ""
        command = input(prompt).strip()

        execute_command(command)

if __name__ == "__main__":
    clear_screen()
    main()
