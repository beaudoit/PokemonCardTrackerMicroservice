# Name: Tristen Beaudoin
# GitHub Username: beaudoit
# OSU Email: beaudoit@oregonstate.edu
# Course: CS 361 - Software Engineering I
# Project: Pokemon Card Tracker - Ultra-Rare Calculator Microservice
# File Name: test.py
# Description: Test program for the pct_rare_calculator.py microservice.
#              Emulates multiple requests made by the Pokemon Card Tracker main program.

COMMS_FILE = "pct_rare_calculator_comms.txt"
ACTION = "calculate_ultra_rare_plus"
SET = "151"

import json, time

def send_request(collection):
    request = {
        "action": ACTION,
        "set": SET,
        "collection": collection
    }

    request_json = json.dumps(request)

    with open(COMMS_FILE, "w") as file:
        file.write(request_json)

    return request

# No ultra-rare+ cards
collection1 = [
    { "name": "Bulbasaur", "set": "151", "number": "001/165", "rarity": "Common" },
    { "name": "Ivysaur", "set": "151", "number": "002/165", "rarity": "Uncommon" },
    { "name": "Venusaur ex", "set": "151", "number": "003/165", "rarity": "Rare" },
    { "name": "Charmander", "set": "151", "number": "004/165", "rarity": "Common" },
    { "name": "Charmeleon", "set": "151", "number": "005/165", "rarity": "Uncommon" },
    { "name": "Charizard ex", "set": "151", "number": "006/165", "rarity": "Rare" },
    { "name": "Squirtle", "set": "151", "number": "007/165", "rarity": "Common" },
    { "name": "Wartortle", "set": "151", "number": "008/165", "rarity": "Uncommon" },
    { "name": "Blastoise ex", "set": "151", "number": "009/165", "rarity": "Rare" }
  ]

# All ultra-rare+ cards
collection2 = [
    {"name": "Bulbasaur", "set": "151", "number": "166/165", "rarity": "Illustration Rare"},
    {"name": "Ivysaur", "set": "151", "number": "167/165", "rarity": "Illustration Rare"},
    {"name": "Charmander", "set": "151", "number": "168/165", "rarity": "Illustration Rare"},
    {"name": "Charmeleon", "set": "151", "number": "169/165", "rarity": "Illustration Rare"},
    {"name": "Squirtle", "set": "151", "number": "170/165", "rarity": "Illustration Rare"},
    {"name": "Wartortle", "set": "151", "number": "171/165", "rarity": "Illustration Rare"},
    {"name": "Caterpie", "set": "151", "number": "172/165", "rarity": "Illustration Rare"},
    {"name": "Pikachu", "set": "151", "number": "173/165", "rarity": "Illustration Rare"},
    {"name": "Nidoking", "set": "151", "number": "174/165", "rarity": "Illustration Rare"},
    {"name": "Psyduck", "set": "151", "number": "175/165", "rarity": "Illustration Rare"},
    {"name": "Poliwhirl", "set": "151", "number": "176/165", "rarity": "Illustration Rare"},
    {"name": "Machoke", "set": "151", "number": "177/165", "rarity": "Illustration Rare"},
    {"name": "Tangela", "set": "151", "number": "178/165", "rarity": "Illustration Rare"},
    {"name": "Mr. Mime", "set": "151", "number": "179/165", "rarity": "Illustration Rare"},
    {"name": "Omanyte", "set": "151", "number": "180/165", "rarity": "Illustration Rare"},
    {"name": "Dragonair", "set": "151", "number": "181/165", "rarity": "Illustration Rare"},

    {"name": "Arbok ex", "set": "151", "number": "182/165", "rarity": "Ultra Rare"},
    {"name": "Ninetales ex", "set": "151", "number": "183/165", "rarity": "Ultra Rare"},
    {"name": "Wigglytuff ex", "set": "151", "number": "184/165", "rarity": "Ultra Rare"},
    {"name": "Golem ex", "set": "151", "number": "185/165", "rarity": "Ultra Rare"},
    {"name": "Kangaskhan ex", "set": "151", "number": "186/165", "rarity": "Ultra Rare"},
    {"name": "Jynx ex", "set": "151", "number": "187/165", "rarity": "Ultra Rare"},
    {"name": "Mew ex", "set": "151", "number": "188/165", "rarity": "Ultra Rare"},
    {"name": "Machamp ex", "set": "151", "number": "189/165", "rarity": "Ultra Rare"},
    {"name": "Dodrio ex", "set": "151", "number": "190/165", "rarity": "Ultra Rare"},
    {"name": "Electrode ex", "set": "151", "number": "191/165", "rarity": "Ultra Rare"},
    {"name": "Gengar ex", "set": "151", "number": "192/165", "rarity": "Ultra Rare"},
    {"name": "Snorlax ex", "set": "151", "number": "193/165", "rarity": "Ultra Rare"},
    {"name": "Dragonite ex", "set": "151", "number": "194/165", "rarity": "Ultra Rare"},
    {"name": "Moltres ex", "set": "151", "number": "195/165", "rarity": "Ultra Rare"},
    {"name": "Articuno ex", "set": "151", "number": "196/165", "rarity": "Ultra Rare"},
    {"name": "Zapdos ex", "set": "151", "number": "197/165", "rarity": "Ultra Rare"},

    {"name": "Venusaur ex", "set": "151", "number": "198/165", "rarity": "Special Illustration Rare"},
    {"name": "Charizard ex", "set": "151", "number": "199/165", "rarity": "Special Illustration Rare"},
    {"name": "Blastoise ex", "set": "151", "number": "200/165", "rarity": "Special Illustration Rare"},
    {"name": "Alakazam ex", "set": "151", "number": "201/165", "rarity": "Special Illustration Rare"},
    {"name": "Zapdos ex", "set": "151", "number": "202/165", "rarity": "Special Illustration Rare"},
    {"name": "Erika's Invitation", "set": "151", "number": "203/165", "rarity": "Special Illustration Rare"},
    {"name": "Giovanni's Charisma", "set": "151", "number": "204/165", "rarity": "Special Illustration Rare"},

    {"name": "Mew ex", "set": "151", "number": "205/165", "rarity": "Hyper Rare"},
    {"name": "Switch", "set": "151", "number": "206/165", "rarity": "Hyper Rare"},
    {"name": "Basic Energy", "set": "151", "number": "207/165", "rarity": "Hyper Rare"}
]

# Mix of common and ultra-rare+ cards, but all from set 151
collection3 = [
    { "name": "Bulbasaur", "set": "151", "number": "001/165", "rarity": "Common" },
    { "name": "Charmander", "set": "151", "number": "004/165", "rarity": "Common" },
    { "name": "Squirtle", "set": "151", "number": "007/165", "rarity": "Common" },
    { "name": "Pidgey", "set": "151", "number": "016/165", "rarity": "Common" },
    { "name": "Rattata", "set": "151", "number": "019/165", "rarity": "Common" },
    { "name": "Mew ex", "set": "151", "number": "205/165", "rarity": "Hyper Rare" },
    { "name": "Charizard ex", "set": "151", "number": "199/165", "rarity": "Special Illustration Rare" },
    { "name": "Venusaur ex", "set": "151", "number": "182/165", "rarity": "Ultra Rare" },
    { "name": "Blastoise ex", "set": "151", "number": "184/165", "rarity": "Ultra Rare" },
    { "name": "Erika's Invitation", "set": "151", "number": "203/165", "rarity": "Special Illustration Rare" },
    { "name": "Bulbasaur", "set": "151", "number": "166/165", "rarity": "Illustration Rare" },
    { "name": "Charmander", "set": "151", "number": "168/165", "rarity": "Illustration Rare" },
    { "name": "Squirtle", "set": "151", "number": "170/165", "rarity": "Illustration Rare" }
  ]

# Mix of common and ultra-rare+ cards from different sets (not only set 151)
collection4 = [
    { "name": "Charmander", "set": "151", "number": "004/165", "rarity": "Common" },
    { "name": "Squirtle", "set": "151", "number": "007/165", "rarity": "Common" },
    { "name": "Pidgey", "set": "151", "number": "016/165", "rarity": "Common" },
    { "name": "Mew ex", "set": "151", "number": "205/165", "rarity": "Hyper Rare" },
    { "name": "Erika's Invitation", "set": "151", "number": "203/165", "rarity": "Special Illustration Rare" },
    { "name": "Charizard ex", "set": "151", "number": "199/165", "rarity": "Special Illustration Rare" },
    { "name": "Gardevoir ex", "set": "Scarlet & Violet", "number": "086/198", "rarity": "Ultra Rare" },
    { "name": "Mimikyu", "set": "Brilliant Stars", "number": "TG13/TG30", "rarity": "Ultra Rare" },
    { "name": "Squawkabilly", "set": "Paldea Evolved", "number": "SV2-174", "rarity": "Common" },
    { "name": "Pikachu", "set": "151", "number": "173/165", "rarity": "Illustration Rare" }
  ]

collections = [collection1, collection2, collection3, collection4]

if __name__ == "__main__":
    print("\nTest program running. Will send multiple requests to the pct_rare_calculator.py microservice "
          "and print the results.\n")

    collection_counter = 0
    for collection in collections:

        time.sleep(4)

        collection_counter += 1
        print(f"Running test on collection{collection_counter}\n")

        time.sleep(2)

        request = send_request(collection)
        print(f"Sent request:\n\n{request}\n")

        time.sleep(2)

        with open(COMMS_FILE, "r") as file:
            response = json.load(file)
        print(f"Response received:\n\n{response}\n")

        with open(COMMS_FILE, "w") as file:
            file.write("")
