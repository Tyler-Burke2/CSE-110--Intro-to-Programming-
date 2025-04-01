import sys
import time
import random
import subprocess

# Function to check and install a packages
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found, installing it...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check and install the required packages
install_package("rich")
install_package("yaspin")

# Import the required libraries
from rich import print
from yaspin import yaspin

# Chatbot response function without progress bar
def chatbot_response(message, min_speed=0.01, max_speed=0.08, thinking_time=1.0):
    # Spinner for the "thinking" effect
    with yaspin(text="Thinking...", color="cyan") as spinner:
        time.sleep(thinking_time)  # Thinking time
        spinner.text = "Responding..."
        spinner.ok("✔")  # Mark spinner as done with a check mark
        
        # Printing the message character by character
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(random.uniform(min_speed, max_speed))
        print()  # Move to the next line after the message is printed

# Prompt for name
print("[bold cyan]Please enter your name (First and Last):[/bold cyan] ", end="")
name = input()

# Prompt for team name
print("[bold cyan]Please enter your team name:[/bold cyan] ", end="")
team_name = input()

# Confirmation message
confirmation_message = (
    f"Congratulations, {name}! You have successfully installed Python, VS Code, and have access to our class in Microsoft Teams. You've completed the first steps towards becoming a Python programmer. Your part in this assignment is now complete.\n"
    "We have a fun semester ahead of us and I'm thrilled to get to know you better! It's my hope and goal to lift your spirit, build your confidence, encourage you to reach your full potential as a Child of God, and inspire you to leverage the power of technology as a tool for good in the world. I'm looking forward to a great semester filled with the magic of automation with the power and flexibility of Python!"
)

# Ask if the user is the team leader
print("[bold cyan]Are you the team leader? (Yes/No):[/bold cyan] ", end="")
is_team_leader = input().strip().lower()

if is_team_leader == "yes":
    # Team leader instructions
    print("[bold cyan]Please enter the names of your team members, separated by commas: (e.g., John Doe, Jane Doe, etc.)[/bold cyan] ", end="")
    team_members = input()

    team_leader_first_message = (
        f'Congratulations, {name}! Being a leader is a big responsibility. Consider the following message from a wizard, named Albus Dumbledore, “It is a curious thing, Harry, but perhaps those who are best suited to power are those who have never sought it. Those who, like you, have leadership thrust upon them, and take up the mantle because they must, and find to their own surprise that they wear it well.”\n \n'
        'We have a fun semester ahead of us and I\'m thrilled to get to know you better! It\'s my hope and goal to lift your spirit, build your confidence, encourage you to reach your full potential as a Child of God, and inspire you to leverage the power of technology as a tool for good in the world. I\'m looking forward to a great semester filled with the magic of automation with the power and flexibility of Python!\n \n'
        "Please copy/paste the message below into the 'Teach One Another' channel on Microsoft Teams:\n"
    )

    team_leader_teams_message = (
        f"Hello everyone! I'm {name}, the team lead from {team_name}. Our team consists of {team_members}. I've confirmed that each member of my team has downloaded and installed Python, VS Code, and has access to our class in Microsoft Teams. I'm looking forward to a great semester, filled with the magic of automation with Python!"
    )

    # Display team leader messages
    chatbot_response("\n" + team_leader_first_message)
    chatbot_response("\n" + team_leader_teams_message)

elif is_team_leader == "no":
    # Display confirmation message
    chatbot_response("\n" + confirmation_message)

else:
    # Handle invalid input
    print("[bold red]Invalid input. Please run the program again and enter 'Yes' or 'No'[/bold red]")