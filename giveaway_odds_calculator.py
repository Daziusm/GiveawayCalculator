#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Discord Giveaway Calculator
A simple utility to calculate odds of winning Discord giveaways
"""

import argparse
import sys
import math
import os
import random
import webbrowser
from datetime import datetime
import json

VERSION = "1.0.0"

def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the banner for the Discord Giveaway Calculator."""
    print("=" * 64)
    print(f"{'DISCORD GIVEAWAY CALCULATOR':^64}")
    print("=" * 64)
    print(f"{'Version ' + VERSION:^64}")
    print("=" * 64 + "\n")

def calculate_standard_odds(accounts, participants, winners):
    """
    Calculate the odds of winning a standard giveaway.
    
    Args:
        accounts (int): Number of accounts you have entering the giveaway
        participants (int): Total number of participants
        winners (int): Number of winners to be selected
        
    Returns:
        float: Probability of winning as a percentage
    """
    # Basic probability calculation
    if participants <= 0 or winners <= 0 or accounts <= 0:
        return 0
    
    # Make sure winners doesn't exceed participants
    winners = min(winners, participants)
    
    # Calculate probability of winning with multiple accounts
    probability = 1 - (1 - winners/participants) ** accounts
    
    return probability * 100

def calculate_invite_requirement_odds(accounts, participants, winners, invite_threshold=5):
    """
    Calculate odds for giveaways with invite requirements.
    
    Args:
        accounts (int): Number of your accounts
        participants (int): Total number of participants
        winners (int): Number of winners
        invite_threshold (int): Minimum number of invites required
        
    Returns:
        float: Probability of winning as a percentage
    """
    # Assume only 30% of participants have the required invites
    eligible_participants = math.ceil(participants * 0.3)
    
    # Calculate standard odds with the reduced participant pool
    return calculate_standard_odds(accounts, eligible_participants, winners)

def calculate_message_requirement_odds(accounts, participants, winners, message_threshold=10):
    """
    Calculate odds for giveaways with message requirements.
    
    Args:
        accounts (int): Number of your accounts
        participants (int): Total number of participants
        winners (int): Number of winners
        message_threshold (int): Minimum number of messages required
        
    Returns:
        float: Probability of winning as a percentage
    """
    # Assume only 50% of participants have the required message count
    eligible_participants = math.ceil(participants * 0.5)
    
    # Calculate standard odds with the reduced participant pool
    return calculate_standard_odds(accounts, eligible_participants, winners)

def calculate_multiple_requirement_odds(accounts, participants, winners):
    """
    Calculate odds for giveaways with multiple requirements.
    
    Args:
        accounts (int): Number of your accounts
        participants (int): Total number of participants
        winners (int): Number of winners
        
    Returns:
        float: Probability of winning as a percentage
    """
    # Assume only 15% of participants meet all requirements
    eligible_participants = math.ceil(participants * 0.15)
    
    # Calculate standard odds with the reduced participant pool
    return calculate_standard_odds(accounts, eligible_participants, winners)

def calculate_odds(accounts, participants, winners, calculation_type="standard"):
    """
    Calculate odds based on the specified calculation type.
    
    Args:
        accounts (int): Number of your accounts
        participants (int): Total number of participants
        winners (int): Number of winners
        calculation_type (str): Type of calculation to perform
        
    Returns:
        float: Probability of winning as a percentage
    """
    if calculation_type == "standard":
        return calculate_standard_odds(accounts, participants, winners)
    elif calculation_type == "invite":
        return calculate_invite_requirement_odds(accounts, participants, winners)
    elif calculation_type == "message":
        return calculate_message_requirement_odds(accounts, participants, winners)
    elif calculation_type == "multiple":
        return calculate_multiple_requirement_odds(accounts, participants, winners)
    else:
        return calculate_standard_odds(accounts, participants, winners)

def interactive_mode():
    """Run the calculator in interactive mode."""
    clear_screen()
    print_banner()
    
    try:
        print("Enter the following information to calculate your odds:\n")
        
        accounts = int(input("Number of accounts you have entering: "))
        participants = int(input("Total number of participants: "))
        winners = int(input("Number of winners to be selected: "))
        
        print("\nSelect calculation type:")
        print("1. Standard Giveaway")
        print("2. With Invite Requirements")
        print("3. With Message Requirements")
        print("4. With Multiple Requirements")
        
        calc_choice = input("\nEnter choice (1-4): ")
        
        calc_type = "standard"
        if calc_choice == "2":
            calc_type = "invite"
        elif calc_choice == "3":
            calc_type = "message"
        elif calc_choice == "4":
            calc_type = "multiple"
        
        odds = calculate_odds(accounts, participants, winners, calc_type)
        
        clear_screen()
        print_banner()
        print("CALCULATION RESULTS\n")
        print(f"Accounts: {accounts}")
        print(f"Total Participants: {participants}")
        print(f"Winners: {winners}")
        print(f"Calculation Type: {calc_type.capitalize()}")
        print(f"\nYour odds of winning: {odds:.4f}%")
        
        if calc_type != "standard":
            print("\nNote: This calculation assumes certain percentages of")
            print("participants meet the requirements.")
        
        print("\nPress Enter to return to the main menu...")
        input()
    except ValueError:
        print("\nError: Please enter valid numbers.")
        print("\nPress Enter to return to the main menu...")
        input()

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        clear_screen()
        print_banner()
        
        print("Select an option:")
        print("1. Calculate Giveaway Odds")
        print("2. Open Web Interface")
        print("3. View Help and Documentation")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ")
        
        if choice == "1":
            interactive_mode()
        elif choice == "2":
            # Open the HTML interface
            print("\nOpening web interface...")
            open_web_interface()
            print("\nPress Enter to return to the main menu...")
            input()
        elif choice == "3":
            show_help()
            print("\nPress Enter to return to the main menu...")
            input()
        elif choice == "4":
            print("\nThank you for using Discord Giveaway Calculator!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Press Enter to try again...")
            input()

def open_web_interface():
    """Open the HTML interface in the default web browser."""
    html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    if os.path.exists(html_path):
        webbrowser.open('file://' + os.path.abspath(html_path))
    else:
        print(f"Error: Could not find {html_path}")

def show_help():
    """Display help information."""
    clear_screen()
    print_banner()
    
    print("HELP AND DOCUMENTATION\n")
    print("Discord Giveaway Calculator helps you calculate your odds of winning")
    print("giveaways with various requirements.\n")
    
    print("CALCULATION TYPES:")
    print("1. Standard Giveaway: Basic probability calculation")
    print("2. With Invite Requirements: Assumes 30% of participants meet invite requirements")
    print("3. With Message Requirements: Assumes 50% of participants meet message requirements")
    print("4. With Multiple Requirements: Assumes 15% of participants meet all requirements\n")
    
    print("COMMAND LINE USAGE:")
    print("python giveaway_odds_calculator.py --accounts 1 --participants 100 --winners 1")
    print("Optional: --type [standard|invite|message|multiple]")
    
def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Discord Giveaway Calculator")
    
    parser.add_argument("--accounts", type=int, default=1,
                        help="Number of accounts you have entering")
    parser.add_argument("--participants", type=int, default=100,
                        help="Total number of participants")
    parser.add_argument("--winners", type=int, default=1,
                        help="Number of winners to be selected")
    parser.add_argument("--type", type=str, default="standard",
                        choices=["standard", "invite", "message", "multiple"],
                        help="Type of calculation to perform")
    parser.add_argument("--web-ui", action="store_true",
                        help="Open the web interface")
    
    return parser.parse_args()

def main():
    """Main entry point for the Discord Giveaway Calculator."""
    # Parse command-line arguments
    args = parse_arguments()
    
    # If web-ui flag is set, open the web interface
    if args.web_ui:
        open_web_interface()
        return
    
    # Check if any arguments were provided, otherwise launch interactive menu
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] == "--web-ui"):
        main_menu()
    else:
        # Calculate odds based on provided arguments
        odds = calculate_odds(
            args.accounts, 
            args.participants, 
            args.winners, 
            args.type
        )
        
        # Display results
        clear_screen()
        print_banner()
        print("CALCULATION RESULTS\n")
        print(f"Accounts: {args.accounts}")
        print(f"Total Participants: {args.participants}")
        print(f"Winners: {args.winners}")
        print(f"Calculation Type: {args.type.capitalize()}")
        print(f"\nYour odds of winning: {odds:.4f}%")
        
        if args.type != "standard":
            print("\nNote: This calculation assumes certain percentages of")
            print("participants meet the requirements.")

if __name__ == "__main__":
    main()
