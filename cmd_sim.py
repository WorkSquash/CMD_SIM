import os
import random
import string
import time
from datetime import datetime

class CmdSimulator:
    def __init__(self):
        self.commands = {
            'help': self.show_help,
            'echo': self.echo,
            'exit': self.exit_cmd,
            'ls': self.list_files,
            'dir': self.list_files,
            'version': self.show_version,
            'joke': self.tell_joke,
            'date': self.show_date,
            'quote': self.show_quote,
            'calc': self.calculate,
            'weather': self.get_weather,
            'greet': self.greet,
            'time': self.show_time,
            'reverse': self.reverse_text,
            'uppercase': self.uppercase_text,
            'lowercase': self.lowercase_text,
            'count': self.count_characters,
            'sayhi': self.say_hi,
            'random': self.random_value,
            'shutdown': self.shutdown,
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'fortune': self.fortune,
            'roll': self.roll,
            'flip': self.flip,
            'current_user': self.current_user,
            'tree': self.tree,  # The new tree command
            '#panic': self.secret_glitch,  # The secret glitch command
            'cls': self.cls  # The new cls command
        }

        self.version = "Cmd Simulator v1.2"
        
        self.tree_facts = [
            "Did you know? A tree can absorb up to 48 pounds of carbon dioxide per year!",
            "Fun fact: The oldest known tree is over 5,000 years old!",
            "Interesting: Trees can communicate with each other using underground fungi.",
            "Did you know? A single tree can produce enough oxygen for two humans to breathe in a year.",
            "Fact: Some trees can live more than a thousand years!"
        ]

        self.jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I told my computer I needed a break, and now it won’t stop sending me KitKat ads!",
            "Why do programmers prefer dark mode? Because light attracts bugs!"
        ]

        self.quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
            "The best way to predict the future is to invent it. - Alan Kay"
        ]

        self.fortunes = [
            "You will have a great day!",
            "A thrilling time is in your immediate future.",
            "Someone will ask you for your opinion today.",
            "A beautiful, smart, and loving person will be coming into your life.",
            "Now is a good time to finance your dreams."
        ]

    def animated_print(self, text, delay=0.05):
        """Print text one character at a time to create an animation effect."""
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()  # For newline at the end

    def cls(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_help(self):
        self.animated_print("Available commands:")
        for command in self.commands:
            self.animated_print(f" - {command}")

    def echo(self, *args):
        """Echos back the provided arguments."""
        self.animated_print(' '.join(args))

    def exit_cmd(self):
        self.animated_print("Exiting the simulator.")
        exit(0)

    def list_files(self):
        """List files in the current directory."""
        self.animated_print("Listing files in the current directory:")
        for item in os.listdir('.'):
            self.animated_print(item)

    def show_version(self):
        """Show the version of the simulator."""
        self.animated_print(self.version)

    def tell_joke(self):
        """Tell a random joke."""
        self.animated_print(random.choice(self.jokes))

    def show_date(self):
        """Display the current date."""
        current_time = datetime.now()
        self.animated_print(current_time.strftime("%Y-%m-%d"))

    def show_quote(self):
        """Show a random quote."""
        self.animated_print(random.choice(self.quotes))

    def calculate(self, *args):
        """Evaluate a simple mathematical expression."""
        expression = ' '.join(args)
        try:
            result = eval(expression)
            self.animated_print("Result: " + str(result))
        except Exception as e:
            self.animated_print(f"Error in calculation: {e}")

    def get_weather(self, city):
        """Simulate fetching weather data for a city."""
        self.animated_print(f"Fetching weather data for {city}...")
        mock_response = {
            "New York": "25°C, Sunny",
            "Los Angeles": "22°C, Clear",
            "Chicago": "15°C, Cloudy",
            "Miami": "30°C, Humid"
        }
        self.animated_print(mock_response.get(city, "Weather data not available for that city."))

    def greet(self):
        """Greet the user."""
        self.animated_print("Hello! Hope you're having a great day!")

    def show_time(self):
        """Display the current system time."""
        current_time = datetime.now()
        self.animated_print(current_time.strftime("%H:%M:%S"))

    def reverse_text(self, *args):
        """Reverse the provided text."""
        text = ' '.join(args)
        self.animated_print(text[::-1])

    def uppercase_text(self, *args):
        """Convert the provided text to uppercase."""
        text = ' '.join(args)
        self.animated_print(text.upper())

    def lowercase_text(self, *args):
        """Convert the provided text to lowercase."""
        text = ' '.join(args)
        self.animated_print(text.lower())

    def count_characters(self, *args):
        """Count the number of characters in the provided text."""
        text = ' '.join(args)
        self.animated_print("Character count: " + str(len(text)))

    def say_hi(self, name):
        """Greet a person by name."""
        self.animated_print(f"Hi, {name}! Nice to meet you!")

    def random_value(self, type_value, *args):
        """Generate a random value based on the type specified."""
        if type_value == 'int':
            if len(args) == 2:
                try:
                    start = int(args[0])
                    end = int(args[1])
                    self.animated_print("Random Integer: " + str(random.randint(start, end - 1)))  # end is exclusive
                except ValueError:
                    self.animated_print("Please provide valid integer values.")
            else:
                self.animated_print("Usage: random int <start> <end>")
        elif type_value == 'float':
            if len(args) == 3:
                try:
                    start = float(args[0])
                    end = float(args[1])
                    round_to = int(args[2])
                    random_float = random.uniform(start, end)
                    self.animated_print("Random Float: " + str(round(random_float, round_to)))  # round to specified decimal places
                except ValueError:
                    self.animated_print("Please provide valid float values and rounding.")
            else:
                self.animated_print("Usage: random float <start> <end> <round>")
        elif type_value == 'str':
            if len(args) == 2:
                try:
                    min_length = int(args[0])
                    max_length = int(args[1])
                    if min_length < 1 or max_length < min_length:
                        self.animated_print("Invalid length range.")
                        return
                    length = random.randint(min_length, max_length)
                    random_string = ''.join(random.choices(string.ascii_letters, k=length))
                    self.animated_print("Random String: " + random_string)
                except ValueError:
                    self.animated_print("Please provide valid integer values for lengths.")
            else:
                self.animated_print("Usage: random str <min_char> <max_char>")
        else:
            self.animated_print("Invalid type. Use int, float, or str.")

    def shutdown(self, joke='false'):
        """Shutdown the system or logoff, based on the joke parameter."""
        if joke.lower() == 'true':
            self.animated_print("Shutting down the computer...")
            self.animated_print("Just kidding! Your computer is safe and sound! 😄")
        else:
            self.animated_print("Shutting down the system.")
            # Uncomment the line below to actually shut down the system.
            os.system("shutdown /s /t 1" if os.name == 'nt' else "shutdown -h now")
            self.animated_print("Shutdown command executed.")  # Placeholder to show intended action

    def add(self, num1, num2):
        """Add two numbers."""
        try:
            result = float(num1) + float(num2)
            self.animated_print("Result: " + str(result))
        except ValueError:
            self.animated_print("Please provide two valid numbers.")

    def subtract(self, num1, num2):
        """Subtract one number from another."""
        try:
            result = float(num1) - float(num2)
            self.animated_print("Result: " + str(result))
        except ValueError:
            self.animated_print("Please provide two valid numbers.")

    def multiply(self, num1, num2):
        """Multiply two numbers."""
        try:
            result = float(num1) * float(num2)
            self.animated_print("Result: " + str(result))
        except ValueError:
            self.animated_print("Please provide two valid numbers.")

    def divide(self, num1, num2):
        """Divide one number by another."""
        try:
            num1, num2 = float(num1), float(num2)
            if num2 == 0:
                self.animated_print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                self.animated_print("Result: " + str(result))
        except ValueError:
            self.animated_print("Please provide two valid numbers.")

    def fortune(self):
        """Display a random fortune message."""
        self.animated_print(random.choice(self.fortunes))

    def roll(self, sides):
        """Simulate rolling a die with given sides."""
        try:
            sides = int(sides)
            if sides <= 0:
                self.animated_print("The number of sides must be a positive integer.")
            else:
                result = random.randint(1, sides)
                self.animated_print(f"You rolled a {result} on a {sides}-sided die.")
        except ValueError:
            self.animated_print("Please enter a valid number of sides.")

    def flip(self):
        """Simulate flipping a coin."""
        self.animated_print("Flipping a coin...")
        result = "Heads!" if random.choice([True, False]) else "Tails!"
        self.animated_print(result)

    def current_user(self):
        """Display the current user of the system."""
        username = os.getlogin()
        self.animated_print(f"Current user: {username}")

    def secret_glitch(self):
        """Secretly terminate the script."""
        self.animated_print("Executing secret glitch!")
        self.animated_print("Error: Unexpected condition encountered. Terminating...")
        os._exit(0)  # Force exit the script

    def tree(self):
        """Display the directory tree with a twist."""
        def print_tree(root, prefix=""):
            items = os.listdir(root)
            for i, item in enumerate(items):
                path = os.path.join(root, item)
                is_last = i == len(items) - 1
                # Print the tree structure
                self.animated_print(prefix + ("└── " if is_last else "├── ") + item)
                if os.path.isdir(path):
                    print_tree(path, prefix + ("    " if is_last else "│   "))  # Recursive call for subdirectories

        self.animated_print("Directory structure:")
        print_tree(".")
        self.animated_print("\n--- Fun Tree Fact ---")
        self.animated_print(random.choice(self.tree_facts))
        self.animated_print("---------------------")

    def run(self):
        self.animated_print("Welcome to the Cmd Simulator!")
        self.animated_print("Type 'help' for a list of commands.")
        
        while True:
            user_input = input("> ")
            self.process_input(user_input)

    def process_input(self, input_str):
        parts = input_str.strip().split()
        command = parts[0]

        if command in self.commands:
            self.commands[command](*parts[1:])
        else:
            self.animated_print(f"Command not found: {command}. Type 'help' for available commands.")

if __name__ == "__main__":
    simulator = CmdSimulator()
    simulator.run()