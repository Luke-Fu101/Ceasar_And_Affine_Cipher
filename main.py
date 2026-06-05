from ciphers import caesar_cipher
from ciphers import affine_cipher
import sys
import random
print("EXECUTIVE PYTHON PATH:", sys.executable)
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich.table import Table

console = Console()

def display_welcome_banner():
    console.clear()
    console.rule("[bold red]CLASSICAL CRYPTOGRAPHY ENGINE[/bold red]")
    console.print("\n")

def run_menu():
    while True:
        display_welcome_banner()
        
        # Display options in a styled block
        console.print("[bold green]1.[/bold green] Caesar Cipher (Shift Transformation)")
        console.print("[bold green]2.[/bold green] Affine Cipher (Linear Transformation)")
        console.print("[bold red]3.[/bold red] Exit Engine\n")
        
        # Enforce strict input logic using Prompt
        choice = Prompt.ask("Select an option", choices=["1", "2", "3"])
        
        if choice == "1":
            handle_caesar()
        elif choice == "2":
            handle_affine()
        elif choice == "3":
            console.print("[bold orange]Shutting down engine...[/]")
            sys.exit()

def handle_caesar():
    console.clear()
    console.rule("[bold magenta]Vector: Caesar Cipher[/]")
    
    # 1. Collect inputs cleanly
    text = Prompt.ask("Enter plaintext:")
    shift = random.randint(1, 25)  # For demonstration, we can randomize the shift or ask user for it
    console.print(f"Using a random shift of: [bold cyan]{shift}[/]")
    
    # 2. Compute via your ciphers.py engine
    ciphertext = caesar_cipher(text, shift)
    
    # 3. Present outputs back into Rich Panels
    console.print("\n")
    console.print(Panel(f"[bold white]{ciphertext}[/]", title="[bold green]Generated Ciphertext[/]", expand=False))
    
    Prompt.ask("\nPress Enter to return to main sequence")

def handle_affine():
    console.clear()
    console.rule("[bold magenta]Vector: Affine Cipher[/]")
    
    text = Prompt.ask("Enter plaintext:")
    shift = random.randint(1, 25)
    multiplier = random.choice([1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23])
    console.print(f"Using a random shift of: [bold cyan]{shift}[/]")
    console.print(f"Using a random multiplier of: [bold cyan]{multiplier}[/]")
    
    # Compute the ciphertext
    ciphertext = affine_cipher(text, shift, multiplier)
    console.print("\n")
    console.print(Panel(f"[bold white]{ciphertext}[/]", title="[bold green]Generated Ciphertext[/]", expand=False))
    
    Prompt.ask("\nPress Enter to return to main sequence")
    # Wrap the affine_cipher execution inside a try/except block 
    # to catch the ValueError you raised for invalid multipliers!
    try:
        ciphertext = affine_cipher(text, shift, multiplier)
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        Prompt.ask("\nPress Enter to return to main sequence")
        return

if __name__ == "__main__":
    run_menu()