# Name: Tristen Beaudoin
# GitHub Username: beaudoit
# OSU Email: beaudoit@oregonstate.edu
# Course: CS 361 - Software Engineering I
# Project: Pokemon Card Tracker - Ultra-Rare Calculator Microservice
# File Name: pct_rare_calculator.py
# Description: Microservice that compares a given Pokemon card collection against the cards in a given set that are
#              ultra-rare or higher. Calculates the percentage of ultra-rare+ cards in that set that have been collected
#              and returns various statistics as well as the ultra-rare+ cards that are still missing.
#              Uses a text file as the communication pipeline with the main program.

import json, time

CARD_DATABASE = "cards.json" # JSON record of all cards that need to be referenced
COMMS_FILE = "pct_rare_calculator_comms.txt" # Name of file to read/write to for comms pipeline with main program
# Rarity statuses considered ultra-rare+
HIGH_RARITIES = ["Illustration Rare", "Special Illustration Rare", "Ultra Rare","Hyper Rare"]
DELAY = 1 # Polling rate to check comms file for new request

def calculate_ultra_rare_plus(card_set, collection):
    # Create a list of the numbers of all ultra-rare+ cards that are from the given set
    set_ultra_rare_plus_numbers = []
    for card in ultra_rare_plus:
        if card["set"] == card_set:
            set_ultra_rare_plus_numbers.append(card["number"])

    # Create a list of the numbers of all cards in the collection that are from the given set
    collection_card_numbers = []
    for card in collection:
        if card["set"] == card_set:
            collection_card_numbers.append(card["number"])

    count_ultra_rare_plus_set = len(set_ultra_rare_plus_numbers) # Find the number of ultra-rare+ cards in that set
    count_ultra_rare_plus_collected = 0
    missing_ultra_rare_plus = []
    for card_number in set_ultra_rare_plus_numbers:
        # If the ultra-rare+ card exists in the collection, increment the count of ultra-rare+ cards collected
        if card_number in collection_card_numbers:
            count_ultra_rare_plus_collected += 1
        # If the ultra-rare+ card doesn't exist, find the complete card entry and append it to the list of missing cards
        else:
            for card in ultra_rare_plus:
                if card["number"] == card_number:
                    missing_ultra_rare_plus.append(card)
                    break

    percentage_collected = count_ultra_rare_plus_collected / count_ultra_rare_plus_set # Calculate percentage collected
    rounded_percentage = round(percentage_collected, 4)

    # Package up all required data in a dictionary to be later sent as JSON
    result = {
        "percentage_collected": rounded_percentage,
        "total_cards": count_ultra_rare_plus_set,
        "collected_cards": count_ultra_rare_plus_collected,
        "missing_cards": missing_ultra_rare_plus
    }

    return result

if __name__ == "__main__":
    print("\nUltra-rare+ calculator microservice running. "
          "Waiting for requests from Pokemon Card Tracker main program.\n\n")

    # Open JSON file and store contents as the database of all cards to be referenced
    with open(CARD_DATABASE, "r") as file:
        card_database = json.load(file)

    # Filter out all ultra-rare+ cards from the database and store in separate list
    ultra_rare_plus = []
    for card in card_database:
        if card["rarity"] in HIGH_RARITIES:
            ultra_rare_plus.append(card)

    # Create or clear the comms file
    with open(COMMS_FILE, "w") as file:
        file.write("")

    while True:
        # Poll comms file looking for request, waiting the standard delay and providing visual indicator
        time.sleep(DELAY)
        print(".")

        # Check file for content
        with open(COMMS_FILE, "r") as file:
            content = file.read().strip()

        if not content:
            continue

        # If file has content, begin processing
        try:
            message = json.loads(content)
            # If file has an "action" key, then it must be a request from the main program
            if message.get("action"):
                action = message["action"]
                card_set = message["set"]
                collection = message["collection"]

                print(f"'{action}' request received from main program.\n\n")

                # Check requested action
                if action == "calculate_ultra_rare_plus":

                    result = calculate_ultra_rare_plus(card_set, collection)

                    result_json = json.dumps(result) # Convert dictionary result to JSON

                    # Overwrite comms file with response
                    with open(COMMS_FILE, "w") as file:
                        file.write(result_json)

                    print("Calculations complete and response sent to main program.\n\n")

                else:
                    print(f"Error: '{action}' request not recognized.\n\n")

        except Exception as error:
            print(f"Error: {error}.\n\n")
            continue
