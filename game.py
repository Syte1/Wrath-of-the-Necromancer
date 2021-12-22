"""
Wrath of the Necromancer
"""

import itertools
import random
from copy import deepcopy
import time


def clear_console() -> None:
    """
    Clear the console by printing 100 lines.

    :postcondition: print 100 blank print()s
    :return:
    """
    for i in range(100):
        print()


def intro_sequence() -> None:
    """
    Print intro ASCII.

    :postcondition: prints game logo
    :return:
    """
    print(color_text(r"""
              __     __  ______  ______  ______  __  __                                        
             /\ \  _ \ \/\  == \/\  __ \/\__  _\/\ \_\ \                                       
             \ \ \/ ".\ \ \  __<\ \  __ \/_/\ \/\ \  __ \                                      
              \ \__/".~\_\ \_\ \_\ \_\ \_\ \ \_\ \ \_\ \_\                                     
               \/_/   \/_/\/_/ /_/\/_/\/_/  \/_/  \/_/\/_/                                     
                                                                                               
                  ______  ______     ______  __  __  ______                                    
                 /\  __ \/\  ___\   /\__  _\/\ \_\ \/\  ___\                                   
                 \ \ \/\ \ \  __\   \/_/\ \/\ \  __ \ \  __\                                   
                  \ \_____\ \_\        \ \_\ \ \_\ \_\ \_____\                                 
                   \/_____/\/_/         \/_/  \/_/\/_/\/_____/                                 
                                                                                               
 __   __  ______  ______  ______  ______  __    __  ______  __   __  ______  ______  ______    
/\ "-.\ \/\  ___\/\  ___\/\  == \/\  __ \/\ "-./  \/\  __ \/\ "-.\ \/\  ___\/\  ___\/\  == \   
\ \ \-.  \ \  __\\ \ \___\ \  __<\ \ \/\ \ \ \-./\ \ \  __ \ \ \-.  \ \ \___\ \  __\\ \  __<   
 \ \_\\"\_\ \_____\ \_____\ \_\ \_\ \_____\ \_\ \ \_\ \_\ \_\ \_\\"\_\ \_____\ \_____\ \_\ \_\ 
  \/_/ \/_/\/_____/\/_____/\/_/ /_/\/_____/\/_/  \/_/\/_/\/_/\/_/ \/_/\/_____/\/_____/\/_/ /_/ 
""", [255, 5, 5]))


def ending_sequence(character) -> None:
    """
    Print ending sequence ascii and character info.

    :param character: a dictionary
    :precondition: character dictionary contains keys "Name"(str), "Class"(str), "Current HP"(int),
                    "Max HP"(int), "Level"(int), "Experience"(int), "Level up XP"(int),
                    "Damage"(int), and "Accuracy"(int)
    :postcondition: print victory ascii, a message, and the character's stats
    :return:
    """
    print(r"  _   __   _        __                   ")
    print(r" | | / /  (_) ____ / /_ ___   ____  __ __")
    print(r" | |/ /  / / / __// __// _ \ / __/ / // /")
    print(r" |___/  /_/  \__/ \__/ \___//_/    \_, / ")
    print(r"                                  /___/  ")

    print(F"You have defeated the necromancer and avenged your comrades, {character['Name']}!\n")
    show_status(character)


def save_path(character: dict) -> None:
    """
    Save character's current coordinates to character's dictionary.

    :param character: a dictionary
    :precondition: dictionary contains the key "Saved path" as a list
    :postcondition: append the current coordinate of the character to the dictionary key
                    "Saved path"
    :return:
    >>> example_character = {'Name': 'Belal', 'X-Coordinate': 12,'Y-Coordinate': 20, \
    'Saved path': []}
    >>> save_path(example_character)
    >>> print(example_character)
    {'Name': 'Belal', 'X-Coordinate': 12, 'Y-Coordinate': 20, 'Saved path': [(12, 20)]}
    """
    character["Saved path"].append((character["X-Coordinate"], character["Y-Coordinate"]))


def print_map_location_character(board: dict, character: dict) -> None:
    """
    Print the board, the status and the location of the character.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board dictionary must contain tuples containing two integers that represent
                    coordinates on a map, with values as integers 1, 2, 3, 4 or strings "t" or "B"
    :precondition: character dictionary must contain keys "X-Coordinate" and "Y-Coordinate" with
                    integer values corresponding to a location that exists on the board.
    :precondition: character dictionary must include keys "Name"(str), "Class"(str),
                    "Current HP"(int), "Max HP"(int), "Level"(int), "Experience"(int),
                    "Level up XP"(int), "Damage"(int), and "Accuracy"(int)
    :postcondition: prints the board, a description of the current location, and the character's
                    status
    :return:
    """
    print_board(board, character)
    describe_current_location(board, character)
    describe_character_status(character)


def show_status(character) -> None:
    """
    Print character's status then prompt to continue.

    :param character: a dictionary
    :precondition: character dictionary must include keys "Name"(str), "Class"(str),
                    "Current HP"(int), "Max HP"(int), "Level"(int), "Experience"(int),
                    "Level up XP"(int), "Damage"(int), and "Accuracy"(int)
    :postcondition: prints the character's name, class, hp, max hp, level, experience,
                    level up experience, damage, and accuracy then prompts the user to continue
    :return:
    """
    print(F'\n'
          F'Name: {character["Name"]}\tClass: {character["Class"]}\n'
          F'HP: {character["Current HP"]} / {character["Max HP"]}\n'
          F'Level: {character["Level"]}\t'
          F'Experience: {character["Experience"]} / {character["Level up XP"]}\n'
          F'Damage: {character["Damage"]}\n'
          F'Accuracy: {character["Accuracy"]}')
    prompt_to_continue()


def prompt_to_continue() -> None:
    """
    Prompt the user to press enter.
    :return:
    """
    input("\n press enter to continue\n")


def ask_for_name(character) -> None:
    """
    Prompt the user to input a name and store it into the character's dictionary.

    :param character: a dictionary
    :precondition: character is a dictionary
    :postcondition: prompts the user for a name and stores it into the key "Name"
    :return:
    """
    character["Name"] = input(F'Hello, adventurer. What is your name?')


def print_board(dungeon_map, character) -> None:
    """
    Print the map with colors.

    This function prints a map with colors and leaves the color tag open to continue coloring
    future text.

    :param dungeon_map: a dictionary
    :param character: a dictionary
    :precondition: board dictionary must contain tuples containing two integers that represent
                    coordinates on a map, with values as integers 1, 2, 3, 4 or strings "t" or "B",
                    "V", "H", "+", "B", or "@"
    :precondition: character must contain keys "X-Coordinate" and "Y-Coordinate" as integers that
                    correspond to existing locations on the board.
    :postcondition: prints a colored map with the character's location included
    :postcondition: leave the color tag open to continue coloring future print statements in the
                    same color scheme.
    :return:
    """
    level_color = determine_level_color(character)
    # copy map to modify it safely
    copied_map = deepcopy(dungeon_map)
    # set current coordinate value on map copy as @
    copied_map[(character["X-Coordinate"], character["Y-Coordinate"])] = "@"
    for iterator, coords in enumerate(copied_map):
        choose_color_saved_path(copied_map, coords, character, level_color)
        if not (iterator + 1) % 25:
            # make all tiles right of the board black and new line
            print(F"\033[1;{level_color};40m")
            # keep color open so everything else uses it


def choose_color_saved_path(board: dict, coordinates: tuple, character: dict, level_color):
    """
    Color space on map.

    This function colors a space on a map depending on if the character has been there.
    If the character hasn't been there, it will be colored based on the level of the area the
    character is in. It the spot has been visited, it will be colored in another color.

    :param board: a dictionary
    :param coordinates: a tuple
    :param character: a dictionary
    :param level_color: a number representing a color
    :precondition: board dictionary must contain key tuples that match the coordinates that are
                    listed in the character dictionary key "Saved Path"
    :precondition: coordinates tuple must be a valid tuple that exists as a key in the board
                    dictionary
    :precondition: character dictionary must contain a key "Saved Path" which contains a list of
                    tuples containing two integers that represent X and Y coordinates respectively
    :precondition: level_color must be a number representing a color in Python
    :precondition: board dictionary tuples must contain either a value of 1, 2, 3, 4 as integers or
                    "E", "V", "H", "+", "B", "t", or "@"
    :postcondition: recolors the coordinate symbol on the map to reflect either a visited area or an
                    area that is colored based on the Y-Coordinate of the character
    :return:
    """
    # determines the color of the saved path
    saved_path_color = 37

    if coordinates in character["Saved path"]:
        # if coordinate is in saved path, color it gray
        print(symbol_dictionary(saved_path_color, [board[coordinates]][0]), end="")
    else:
        # color space by level
        print(symbol_dictionary(level_color, [board[coordinates]][0]), end="")


def determine_level_color(character: dict) -> int:
    """
    Determine the text color of the level.

    This function receives a character's coordinates in a dictionary and, depending on their
    Y-Coordinate, returns an integer representing the color of the level of the area they are
    standing in. Green is level 1, yellow is level 2, and red is level 3.

    :param character: A dictionary
    :precondition: character dictionary must contain key "Y-Coordinate" as a positive integer
    :postcondition: determines the text-color that should be returned that corresponds to the
                    difficulty of the area the player is standing in
    :return: int 32 for level 1, int 33 for level 2. and int 31 for level 3

    # determine the level color of a character at a 0 Y-Coordinate
    >>> print(determine_level_color({"Y-Coordinate": 0}))
    31
    """
    if area_level(character) == 1:  # Level 1 area
        return 32
    elif area_level(character) == 2:  # Level 2 area
        return 33
    else:  # Level 3 area
        return 31


def area_level(character: dict) -> int:
    """
    Determine the area level a character is standing in character.

    :param character: a dictionary
    :precondition: character dictionary must contain key "Y-Coordinate" with a positive integer
                    value
    :postcondition: determines the level of the area the character is standing on.
    :return: 1, 2, or 3 as integer

    # Check the level area of a character standing at Y-Coordinate 16
    >>> area_level({"Y-Coordinate": 16})
    2
    """
    if character["Y-Coordinate"] >= 17:  # Level 1 area
        level = 1
    elif character["Y-Coordinate"] >= 9:  # Level 2 area
        level = 2
    else:  # Level 3 area
        level = 3

    return level


def symbol_dictionary(level_color, actual_symbol):
    """
    Contain a dictionary storing symbols that correspond to elements on the map.

    :param level_color: integer
    :param actual_symbol: integer or string
    :precondition: level color must be integer 31, 32, or 33
    :precondition: actual symbol must be integer 1, 2, 3, or 4 or strings "V", "H", "+", "B", "t",
                    "@"
    :postcondition: determines the colored symbol represented by the actual symbol in the level area
                    color
    :return: 3 character string colored string that visually represents the actual symbol in the
            area level
    >>> symbol_dictionary(3, 3)
    '\x1b[1;3;40m<o>\x1b[0m'
    """
    # store alternative characters to print for map
    symbols = {1: F"\033[1;{level_color};40m,.,\33[0m",
               2: F"\033[1;{level_color};40m','\33[0m",
               3: F"\033[1;{level_color};40m<o>\33[0m",
               4: F"\033[1;{level_color};40m,O.\33[0m",
               "E": F"\033[1;94;40m E \33[0m",
               "V": "\033[1;36;40m | \33[0m",
               "H": "\033[1;36;40m---\33[0m",
               "+": "\033[1;36;40m + \33[0m",
               "B": "\033[1;91;47m B \33[0m",
               "t": "\033[1;35;40m t \33[0m",
               "@": "\033[1;98;40m(*)\33[0m"}

    return symbols[actual_symbol]


def color_text(str_to_color: str, text_color: list):
    """
    Color text.

    This function takes in a string to color and a list containing a red, green, and blue value
    [R, G, B] as integers from 0-255. A colored copy of the string is generated and returned

    :param str_to_color: a string
    :param text_color: a list
    :precondition: str_to_color must be a string
    :precondition: text_color must be a list formatted like [1, 2, 3] where 1 represents red value,
                    2 represents a green value, and 3 represents a red value.
    :precondition: text-color must be a list containing 3 seperated integers from 0-255 inclusive
    :postcondition: a colored copy of the string is generated in the chosen RGB values and chosen
                    color extends to future strings
    :return: colored string
    """
    return F"\33[38;2;{text_color[0]};{text_color[1]};{text_color[2]};40m{str_to_color}"


def print_scenario(character: dict) -> None:
    """
    Print the scenario of a character's class.

    :param character: a dictionary
    :precondition: character dictionary must have a key "Class" that contains a string is either
                    "Knight", "Wizard", "Archer", "Fighter"
    :postcondition: print the scenario of the character's class
    :return:
    """
    if character['Class'] == "Knight":
        first_phrase = F"You know your way around a sword and have a strong sense of justice.\n"
        second_phrase = F"with your sword."
    elif character['Class'] == "Wizard":
        first_phrase = F"You have an expansive understanding of magic and yearn for more of it.\n"
        second_phrase = F"with your powerful magic."
    elif character['Class'] == "Archer":
        first_phrase = F"You're skilled with a bow, have a keen eye and great reflexes.\n"
        second_phrase = F"with your bow."
    else:
        first_phrase = F"You're a tough brawler with huge muscles. You aren't afraid of anything.\n"
        second_phrase = F"with your fists."
    print(color_text(F"You are the {character['Class']} named {character['Name']}.\n"
                     F"{first_phrase}\n"
                     F"Your hometown was ravaged by a necromancer and you are hell-bent\n"
                     F"on avenging your fallen comrades. Your mission is to track down and\n"
                     F"slay the necromancer {second_phrase}\n\n"
                     F"You find yourself in a grassy land.\n"
                     F"The necromancer's castle is north of you. The necromancer was so powerful "
                     F"that\n"
                     F"you had no chance of defeating him in the past, so you will need to\n"
                     F"fight enemies and collect treasure if you want to stand any chance in "
                     F"combat.\n\n"
                     F"You head north to the necromancer's tower.", [50, 130, 255]))
    prompt_to_continue()


def class_info(a_class):
    """
    Return a key from within the shared class dictionary.

    :param a_class: a key
    :precondition: key must be defined in the contained class_dictionary
    :postcondition: picks the value corresponding to the entered key
    :return: value corresponding to the a_class key in the class_dictionary

    >>> class_info("Iron Arm Boxer")
    {'Skills': {'RKO            ': {'Damage Multiplier': 10, 'Cooldown': [8, 8]}}}
    """
    # store all elements defined by a class in a dictionary
    class_dictionary = {"Knight": {"Damage": 3, "Max HP": 23, "Accuracy": 85,
                                   "Skills": {"Slash        ": {"Damage Multiplier": 2,
                                                                "Cooldown": [1, 1]},
                                              "Sword Barrage": {"Damage Multiplier": 3,
                                                                "Cooldown": [3, 3]}}},

                        "Shining Knight": {"Skills": {"Leaping Strike": {"Damage Multiplier": 10,
                                                                         "Cooldown": [6, 6]}}},

                        "Legendary Knight of Honor": {"Skills": {"(Ultimate): Executioner":
                                                                 {"Damage Multiplier": 20,
                                                                  "Cooldown": [10, 10]}}},

                        "Wizard": {"Damage": 4, "Max HP": 10, "Accuracy": 65,
                                   "Skills": {"Firebolt     ": {"Damage Multiplier": 2,
                                                                "Cooldown": [1, 1]},
                                              "Ice Missile  ": {"Damage Multiplier": 4,
                                                                "Cooldown": [4, 4]}}},

                        "Battle Mage": {"Skills": {"Lightning Blast": {"Damage Multiplier": 15,
                                                                       "Cooldown": [10, 10]}}},

                        "Legendary Arcane Master":
                            {"Skills": {"(Ultimate): Orbital Bombardment": {
                                "Damage Multiplier": 30,
                                "Cooldown": [20, 20]}}},

                        "Archer": {"Damage": 3, "Max HP": 15, "Accuracy": 85,
                                   "Skills": {"Quick Shot   ": {"Damage Multiplier": 2,
                                                                "Cooldown": [1, 1]},
                                              "Focused Arrow": {"Damage Multiplier": 3,
                                                                "Cooldown": [3, 3]}}},

                        "Sniper": {"Skills": {"Lightspeed Arrow": {"Damage Multiplier": 8,
                                                                   "Cooldown": [4, 4]}}},

                        "God of Arrows": {"Skills": {"(Ultimate): "
                                                     "Planet Splitter": {"Damage Multiplier": 25,
                                                                         "Cooldown": [15, 15]}}},

                        "Fighter": {"Damage": 3, "Max HP": 30, "Accuracy": 65,
                                    "Skills": {"Jab          ": {"Damage Multiplier": 2,
                                                                 "Cooldown": [1, 1]},
                                               "Haymaker      ": {"Damage Multiplier": 4,
                                                                  "Cooldown": [3, 3]}}},

                        "Iron Arm Boxer": {"Skills": {"RKO            ": {"Damage Multiplier": 10,
                                                                          "Cooldown": [8, 8]}}},

                        "God of Fists": {"Skills": {"(Ultimate): "
                                                    "8th Gate of Hell: Final Burst ":
                                                        {"Damage Multiplier": 20,
                                                         "Cooldown": [15, 15]}}},
                        }

    return class_dictionary[a_class]


def create_character(character: dict):
    """
    Create a character.

    This function asks the user what class they'd like, and updates the given character dictionary
    with the key value pairs necessary for playing the game from level 1.

    :param character: a dictionary
    :precondition: dictionary is valid
    :postcondition: prompt the user to choose a class and populate the character dictionary with the
                    starting key value pairs pertaining to their selected class
    :return:
    """
    available_classes = {"1": "Knight", "2": "Wizard", "3": "Archer", "4": "Fighter"}
    chosen_class = ""
    while chosen_class not in available_classes:
        chosen_class = input(F"What class would you like?\n\n"
                             F"{color_text('[1] - Knight', [255, 255, 1])} "
                             F"- A skilled sword and shield"
                             F" user. Medium damage, and high "
                             F"health points, high accuracy.\n\n"
                             F"{color_text('[2] - Wizard', [58, 137, 255])} "
                             F"- A powerful mage with a book"
                             F" of spells. Very high damage, "
                             F"medium health points, medium accuracy\n\n"
                             F"{color_text('[3] - Archer', [58, 255, 186])} "
                             F"- A skilled archer with a bow"
                             F" and an endless amount of "
                             F"arrows. High damage, medium health points, high accuracy\n\n"
                             F"{color_text('[4] - Fighter', [255, 107, 53])} "
                             F"- A powerful hand to hand"
                             F" fighter. medium damage, very high "
                             F"health points, medium accuracy\n")

    chosen_class = available_classes[chosen_class]
    character.update({"X-Coordinate": 12, "Y-Coordinate": 22,
                      "Class": chosen_class, "Level": 1,
                      "Current HP": class_info(chosen_class)["Max HP"],
                      "Max HP": class_info(chosen_class)["Max HP"],
                      "Damage": class_info(chosen_class)["Damage"],
                      "Accuracy": class_info(chosen_class)["Accuracy"],
                      "Experience": 0, "Level up XP": 100,
                      "Saved path": [],
                      "Skills": class_info(chosen_class)["Skills"]})


def create_initial_board() -> dict:
    """
    Create a board with walls, treasure, and a boss.

    :postcondition: creates a board as a dictionary with keys of tuples representing coordinates,
                    and values corresponding to the things contained at those spots
    :postcondition: creates dictionary with values that contain 1, 2, 3, 4 integers representing
                    different types of rooms, and "V" representing a vertical wall, "H" representing
                    a horizontal wall, "+" representing a joined wall, "t" representing treasure,
                    "B" representing the boss, and @ representing the player
    :return: a board as a dictionary with keys of tuples representing coordinates, and values
            corresponding to the things contained at those spots, that contain 1, 2, 3, 4 integers
            representing different types of rooms, and "V" representing a vertical wall, "H"
            representing a horizontal wall, "+" representing a joined wall, "t" representing
            treasure, "B" representing the boss, and @ representing the player
    """
    dungeon_map = generate_map_spots()
    # pairs of tuples represent full lines from one tuple to the other
    # vertical pairs and horizontal pairs are handled automatically
    walls = [(10, 0), (10, 4),
             (10, 4), (13, 4),
             (15, 4), (16, 4),
             (16, 0), (16, 4),
             (5, 8), (5, 13),
             (5, 13), (10, 13),
             (5, 20), (5, 24),
             (3, 10), (3, 13),
             (20, 10), (24, 10),
             (20, 15), (24, 15),
             (20, 10), (20, 12),
             (20, 14), (20, 15),
             (14, 14), (14, 18),
             (14, 18), (18, 18),
             (23, 1), (23, 7),
             (21, 0), (21, 5),
             (19, 1), (19, 7),
             (19, 7), (23, 7),
             (16, 6), (19, 6),
             (16, 4), (16, 6)]
    create_wall(dungeon_map, walls)
    # boss here
    dungeon_map[(random.randint(11, 15), random.randint(0, 2))] = "B"
    # treasure room
    for treasure in range(15):
        dungeon_map[(random.randint(17, 18), random.randint(1, 5))] = "t"
    # treasure
    generate_treasures(dungeon_map)
    create_exit(dungeon_map)

    return dungeon_map


def create_exit(a_map):
    """
    Create an exit.

    This function receives a map of tuples and assigns them predefined spots as "E" that represents
    exits.

    :param a_map: a dictionary
    :precondition: a_map dictionary must include key tuples containing two integers representing
                    X and Y Coordinates and must include the predefined tuples as keys
    :postcondition: assigns the string "E" to matching tuples in the map dictionary
    """
    # predefined locations as tuples in a list
    exit_locations = [(17, 5), (18, 5)]

    for an_exit in exit_locations:
        a_map[an_exit] = "E"


def generate_treasures(a_map) -> None:
    """
    Generate treasures in a map.

    This function takes a map and psuedo-randomly distributed treasures within certain regions of
    the map.

    :param a_map: a dictionary
    :precondition: dictionary is valid
    :postcondition: creates keys with tuples representing x and y coordinates of treasure and values
                    of "t" and updates them into the map dictionary
    :return:
    """
    small_treasure = 0
    west_side = True
    while small_treasure < 10:
        if west_side:
            x_coords, y_coords = (random.randint(0, 9), random.randint(0, 24))
        else:
            x_coords, y_coords = (random.randint(16, 24), random.randint(0, 24))
        spot = a_map[(x_coords, y_coords)]
        if spot in [1, 2, 3, 4]:
            a_map[x_coords, y_coords] = "t"
            small_treasure += 1
            west_side = not west_side


def create_wall(initial_map: dict, list_of_walls: list) -> None:
    """
    Create horizontal and vertical walls.

    This function takes a map and a list containing tuples representing map coordinates and
    generates walls based on the matching digit in the pair of tuples where the first index
    represents the X-Coordinate and the second index represents the Y-Coordinate.

    :param initial_map: a dictionary
    :param list_of_walls: a list
    :precondition: list_of_walls must be formatted with pairs of tuples that contain non-negative
                    integers where either the first index of each tuple pair or the second index
                    match
    :postcondition: creates vertical walls on the map by setting each tuple in between the pairs
                    with a "V" if their first indexes match and a horizontal wall with a "H" if
                    their second indexes match, and a "+" if a "V" ever overlaps with an "H"
    :return:
    """
    while len(list_of_walls) > 0:
        first_coords = list_of_walls.pop(0)
        second_coords = list_of_walls.pop(0)

        if first_coords[1] == second_coords[1]:
            for x_coord in range(first_coords[0], second_coords[0] + 1):
                if initial_map[(x_coord, first_coords[1])] == "V":
                    initial_map[(x_coord, first_coords[1])] = "+"
                else:
                    initial_map[(x_coord, first_coords[1])] = "H"

        elif first_coords[0] == second_coords[0]:
            for y_coord in range(first_coords[1], second_coords[1] + 1):
                if initial_map[(first_coords[0], y_coord)] == "H":
                    initial_map[(first_coords[0], y_coord)] = "+"
                else:
                    initial_map[(first_coords[0], y_coord)] = "V"


def generate_map_spots() -> dict:
    """
    Create a map of tuples in a 25x25 grid.

    :postcondition: create a dictionary that contains key tuples containing integers representing
                    x and y coordinates.
    :return: a dictionary that contains key tuples containing integers representing x and y
            coordinates
    """
    empty_map = {(x_coord, y_coord): random.randint(1, 4) for y_coord in range(25) for x_coord
                 in range(25)}
    return empty_map


def describe_character_status(character: dict) -> None:
    """
    Print character health points.

    param: character: a character dictionary containing a key for "Current HP"
    :precondition: dictionary is properly formatted
    :postcondition: prints out the current hp of the character
    describe a character with 1 hp
    >>> describe_character_status({"Current HP": 1})
    Current HP: 1
    """
    print(F"\nCurrent HP: {character['Current HP']} / {character['Max HP']}")


def is_dead(character: dict) -> bool:
    """
    Determine if character is dead or alive.

    This function will return True if character is dead and False if alive.

    :param character: a dictionary containing a key for "Current HP"
    :precondition: current HP key is an integer value that's greater than or equal to 0
    :postcondition: determines whether or not the character is dead
    :return: True if dead, False if alive

    check alive player
    >>> is_dead({"Current HP": 1})
    False

    check dead player
    >>> is_dead({"Current HP": 0})
    True
    """
    return character["Current HP"] <= 0


def combat_game(character: dict) -> None:
    """
    Fight an enemy.

    This function receives a character dictionary and generates an enemy based on the character's
    location. The player then fights the enemy until they either decide to run, the character
    decides to run, or one of the combatants are dead.

    :param character: a dictionary
    :precondition: character dictionary must contain keys "Current HP", "Y-Coordinate", "Max HP",
                    "Damage", "Accuracy", "Experience", "Level up XP", and a "Skills" key containing
                    a dictionary of different abilities, with each of those abilities being keys of
                    a dictionary containing keys "Damage Multiplier" and "Cooldown" containing a
                    list of two integers representing current and maximum ability cooldown.
    :postcondition: facilitates a fight between an enemy and a player until one either dies, or runs
                    away
    :return:
    """
    # create an enemy based on y coordinate
    enemy = generate_enemy(character)
    while not is_dead(character):
        print_enemy_encounter(enemy, character)
        selection = choose_fight_option()
        # fight is selected
        if selection == '1':
            attack_enemy(choose_attack(character), enemy, character)
            if is_dead(enemy):
                reward_experience(enemy, character)
                return
            elif enemy_run(enemy):
                return
            enemy_attack(enemy, character)
        # run is selected
        elif selection == '2':
            attempt_to_run(enemy, character)
            return


def enemy_run(enemy: dict) -> bool:
    """
    Determine whether or not an enemy has run away.

    :param enemy: a dictionary
    :precondition: enemy dictionary must contain the key "Name"
    :postcondition: determines if an enemy has run away or not, choosing True 20% of the time if
                    the enemy has run away or choosing False 80% if the enemy has decided not to.
    :return: True 20% of the time, False 80% of the time.
    """
    if enemy["Name"] != "Necromancer":
        if random.choices([True, False], weights=(20, 80))[0]:
            print(F"{enemy['Name']} runs away!")
            # return true if enemy ran
            return True
    else:
        return False


def attempt_to_run(enemy: dict, character: dict) -> None:
    """
    Determine whether or not a character's escape was successful.

    :param enemy: a dictionary
    :param character: a dictionary
    :precondition: enemy dictionary must contain keys "Damage", "Accuracy", "Move",
                    and "Name"
    :precondition: character dictionary must contain keys "Current HP" and "Max HP"
    :postcondition: prints a message that you attempt to run
    :postcondition: rolls a 20/80% chance, 20% returning True and getting hit, and 80% of the time
                    returning False and getting away without taking a hit.
    :postcondition: receive an enemy attack if the roll fails and reduces the character's hp
    :postcondition: prints a message showing the characters hp's if hit, and prints a message
                    stating that the escape was successful
    :return:
    """
    print("You attempt to run")
    time.sleep(1)
    get_hit = random.choices([True, False], weights=[20, 80])[0]
    if get_hit:
        enemy_attack(enemy, character)
        print(F"Current Health: {character['Current HP']} / {character['Max HP']}")
    else:
        print(F"You manage you run away safely")


def reduce_cooldown_heal(character: dict) -> None:
    """
    Regenerate health and advance the cooldown of unavailable abilities.

    :param character: a dictionary
    :precondition: character dictionary must contain key "Skills" which contains an ability key
                    which contains a dictionary containing the the key "Cooldown", which contains
                    a list with the first index being the current cooldown value and the second
                    index being the maximum cooldown.
    :precondition: character dictionary must contain the keys "Current HP", "Max HP", and "Level"
                    containing an integer in each.
    :postcondition: regenerates health of character by 1 per level attained and advances their
                    cooldown by 1 per level attained.
    :return:
    # heal health from 6 to 7
    >>> character_example = {'Level': 1, 'Current HP': 6, 'Max HP': 7, 'Damage': 3, 'Accuracy': 85,\
    'Experience': 0, 'Level up XP': 100, 'Saved path': [(12, 21), (12, 20)], \
    'Skills': {'Quick Shot   ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]}}}
    >>> reduce_cooldown_heal(character_example)
    >>> print(character_example['Current HP'])
    7

    # advance cooldown of quick shot by one step
    >>> character_example = {'Level': 1, 'Current HP': 6, 'Max HP': 7, 'Damage': 3, 'Accuracy': 85,\
    'Experience': 0, 'Level up XP': 100, 'Saved path': [(12, 21), (12, 20)], \
    'Skills': {'Quick Shot   ': {'Damage Multiplier': 2, 'Cooldown': [0, 1]}}}
    >>> reduce_cooldown_heal(character_example)
    >>> print(character_example['Skills']['Quick Shot   ']['Cooldown'][0])
    1
    """
    for skill in character["Skills"]:
        if is_on_cooldown(character, skill):
            # count cooldown up by one
            character["Skills"][skill]["Cooldown"][0] += 1
    # check if health has gone over max
    if character["Current HP"] < character["Max HP"]:
        character["Current HP"] += character["Level"]
        # set cooldown to max
        if character["Current HP"] > character["Max HP"]:
            character["Current HP"] = character["Max HP"]


def reward_experience(enemy: dict, character: dict) -> None:
    """
    Reward character with experience.

    This function rewards the player with experience points. If the character levels up as a result,
    this function will also update many of the character's dictionary values to represent the new
    level.

    :param enemy: a dictionary
    :param character: a dictionary
    :precondition: enemy dictionary must contain keys 'Name', and 'Experience reward'
    :precondition: character dictionary must contain keys "Experience" ,"Level up XP",
                    'Level', "Class", "Skills", "Damage" and "Max HP"
    :postcondition: prints that you've slain the enemy and name it.
    :postcondition: prints amount of experience obtained
    :postcondition: adds experience gained to character dictionary
    :postcondition: levels up the character if level up exp is met
    :postcondition: if level up occurs, adjusts character dictionary keys "Level", "Experience",
                    "Level up XP", "Class", "Skills", "Damage", and "Max HP"
    """
    print(F"\nYou have slain the {enemy['Name']}\n"
          F"Obtained {enemy['Experience reward']} experience\n")
    character["Experience"] += enemy["Experience reward"]
    if character["Experience"] >= character["Level up XP"]:
        level_up(character)


def level_up(character: dict) -> None:
    """
    Level up the character.

    :param character: a dictionary
    :precondition: character dictionary must contain the keys "Level", "Experience", "Level up XP",
                    "Class", "Skills", "Damage", and "Max HP"
    :postcondition: modifies the character dictionary keys "Level", "Experience", "Level up XP",
                    "Class", "Skills", "Damage", and "Max HP" to represent the new level
    :postcondition: prints class that character has leveled to
    :postcondition: prints the learned move gained from leveling up
    """
    character['Level'] += 1
    character["Experience"] -= character["Level up XP"]
    # list of all classes
    class_list = ["Knight", "Shining Knight", "Legendary Knight of Honor",
                  "Wizard", "Battle Mage", "Legendary Arcane Master",
                  "Archer", "Sniper", "God of Arrows",
                  "Fighter", "Iron Arm Boxer", "God of Fists"]
    # store the index of character's class corresponding to the class_list
    class_index = class_list.index(character["Class"])
    # if character is max rank in their class
    if (class_index + 1) % 3 != 0:
        character["Class"] = class_list[class_index + 1]
        character["Skills"].update(class_info(character["Class"])["Skills"])
        time.sleep(1)
        print(F"Leveled up to {character['Class']}!\n")
        time.sleep(1)
        print(F"Learned {[moves for moves in class_info(character['Class'])['Skills']][0]}")
    # executes regardless of max class rank
    character["Level up XP"] *= 9
    character["Damage"] += 6
    character["Max HP"] *= 3
    character["Current HP"] = character["Max HP"]


def attack_enemy(chosen_attack: int, enemy: dict, character: dict) -> None:
    """
    Attack enemy.

    This function handles an attack on an enemy.

    :param chosen_attack: a non-negative integer
    :param enemy: a dictionary
    :param character: a dictionary
    :precondition: chosen_attack must be a non-negative integer
    :precondition: enemy dictionary must contain the key "Current HP"
    :precondition: character dictionary must contain the keys "Skills" which contains a key for a
                    chosen attack which contains the key "Damage Multiplier", and the dictionary
                    must also contain "Accuracy" and "Damage"
    :postcondition: calculate damage dealt by the player
    :postcondition: print that the hit was either accurate or inaccurate
    :postcondition: reduce enemy hp by the damage dealt by the player
    :postcondition: print the move used
    :postcondition: print the amount of damage dealt
    :postcondition: reduce cooldown by the number of levels the character has
    :postcondition: regenerate health by the number of levels the character has
    """
    damage_result = calculate_damage(chosen_attack, character)
    accurate_hit_str = F"It was an inaccurate hit!"
    if damage_result[1]:
        accurate_hit_str = F"It was an accurate hit!"
    enemy["Current HP"] -= damage_result[0]
    print(F"You use {[moves for moves in character['Skills']][chosen_attack - 1]}")
    time.sleep(.5)
    print(F"{accurate_hit_str}\n"
          F"You dealt {damage_result[0]} damage")
    time.sleep(.5)
    reduce_cooldown_heal(character)


def enemy_attack(enemy: dict, character: dict) -> None:
    """
    Handle enemy's attack.

    :param enemy: a dictionary
    :param character: a dictionary
    :precondition: enemy dictionary must contain the keys "Name", "Move", "Accuracy", and "Damage"
                    all containing a non-zero integer respectively
    :precondition: character dictionary must contain the key "Current HP" containing a non-zero
                    integer
    :postcondition: print enemy name and move
    :postcondition: calculate enemy's damage
    :postcondition: print if it was an accurate hit or not
    :postcondition: subtract hp from player equal to the calculated enemy damage
    :postcondition: print the amount of damage the player takes from the attack
    """

    print(F"{enemy['Name']} {enemy['Move']}")
    time.sleep(.5)
    enemy_damage_result = calculate_enemy_damage(enemy)
    character["Current HP"] -= enemy_damage_result[0]
    if enemy_damage_result[1]:
        accurate_hit_str = F"It was an accurate hit!"
        time.sleep(.5)
    else:
        accurate_hit_str = F"It was an inaccurate hit"
        time.sleep(.5)
    print(F"{accurate_hit_str}\n"
          F"You take {enemy_damage_result[0]} damage")
    time.sleep(.5)


def calculate_enemy_damage(enemy: dict) -> tuple:
    """
    Calculate enemy damage.

    This function takes an enemy dictionary and returns whether or not its attack was accurate
    depending on the "Accuracy" key in their dictionary. Once it knows whether or not the ability
    was accurate, it returns a new damage number, lower if the accuracy check failed or higher if it
    was successful.

    :param enemy: a dictionary
    :precondition: enemy dictionary must contain the keys "Accuracy" and "Damage", containing
                    an integer in each, respectively
    :postcondition: determines whether or not the attack was accurate
    :postcondition: calculates damage after accuracy as an integer
    :return: tuple containing an integer in the first index representing damage, and a boolean
             as the second index, representing whether or not the attack was accurate
    """
    accurate_hit = random.choices([True, False], weights=(enemy["Accuracy"],
                                                          (100 - enemy["Accuracy"])))[0]
    raw_damage = enemy["Damage"]
    if accurate_hit:
        return round(raw_damage * (random.randint(11, 13) / 10)), accurate_hit
    else:
        return round(raw_damage * (random.randint(7, 9) / 10)), accurate_hit


def calculate_damage(chosen_attack: int, character: dict) -> tuple:
    """
    Calculate the damage of a character.

    :param chosen_attack: an integer
    :param character: a dictionary
    :precondition: chosen attack must be an integer which corresponds to an index of the character's
                    skills in the dictionary
    :precondition: character dictionary must include keys "Accuracy", "Skills", which contains at
                    least one key corresponding to a skill, each of which, contain a key called
                    "Damage Multiplier" which contains an integer
    :postcondition: determines whether or not the attack was accurate
    :postcondition: calculates damage after accuracy as an integer
    :return: tuple containing an integer in the first index representing damage, and a boolean
             as the second index, representing whether or not the attack was accurate
    """
    accurate_hit = random.choices([True, False], weights=(character["Accuracy"],
                                                          (100 - character["Accuracy"])))[0]
    chosen_attack_name = [moves for moves in character['Skills']][chosen_attack - 1]
    raw_damage = character["Skills"][chosen_attack_name]['Damage Multiplier'] * character['Damage']
    if accurate_hit:
        return round(raw_damage * (random.randint(11, 13) / 10)), accurate_hit
    else:
        return round(raw_damage * (random.randint(7, 9) / 10)), accurate_hit


def choose_attack(character: dict) -> int:
    """
    Prompt the user to select an attack.

    :param character: a dictionary
    :precondition: character dictionary must contain a key "Skills", containing a key representing
                   their chosen ability, which contains the key "Cooldown" which contains a list
                   with integer elements representing cooldown and maximum cooldown.
    :postcondition: print a list of available moves and prompts the user to choose one
    :postcondition: checks if the ability exists or if it's on cooldown
    :postcondition: sets cooldown of ability to 0 if ability is ready
    :return: an integer representing the skill's index in "Skills" dictionary
    """
    available_skills = [moves for moves in character['Skills']]
    print(F"\nAvailable moves:")
    while True:
        skill_choice_number = input(F"{print_skills(character)}")
        # check if input exists in character's skill list
        if skill_choice_number not in list(map(str, range(1, len(character["Skills"]) + 1))):
            print(F"{skill_choice_number} is not a valid attack.")
            continue
        # if the skill is available
        elif not is_on_cooldown(character, available_skills[int(skill_choice_number) - 1]):
            # set the skill on cooldown
            character["Skills"][available_skills[int(skill_choice_number) - 1]]["Cooldown"][0] = 0
            # send the skill used as an index of its spot in the character skills dictionary
            return int(skill_choice_number)
        else:
            print(F"{available_skills[int(skill_choice_number) - 1]} is on cooldown.\n"
                  F"Walk around or use other abilities to refresh it")


def print_skills(character: dict) -> str:
    """
    Print the skills of the character, and their current and maximum cooldowns.

    :param character: a dictionary
    :precondition: character dictionary must contain key "Skills" which contains a dictionary
                    storing keys that represent other abilities which each contain a diction
                    storing a key named "Cooldown" which stores a list with two integer elements
                    which represent current cooldown and maximum cooldown
    :postcondition: prints out the skills of the character, and the current and max cooldowns
                    of each one
    :return: empty string
    """
    for number_of_skill, skill_index in zip(itertools.count(1), character["Skills"]):
        ability_ready = display_cooldown_up(character, skill_index)
        print(F'[{number_of_skill}]\t{skill_index}\t{ability_ready}\tCooldown: '
              F'{character["Skills"][skill_index]["Cooldown"][0]} / '
              F'{character["Skills"][skill_index]["Cooldown"][1]}')
    return ""


def display_cooldown_up(character: dict, skill_to_check: str) -> str:
    """
    Determine if cooldown is up.

    This function takes a character dictionary and a skill, then determines if
    that ability is up and returns a checkmark if it is and an x if it isn't.

    :param character: a dictionary
    :param skill_to_check: a key in a dictionary
    :precondition: character dictionary must contain key "Skills" which contains a dictionary
                storing keys that represent other abilities which each contain a diction
                storing a key named "Cooldown" which stores a list with two integer elements
                which represent current cooldown and maximum cooldown
    :precondition: skill to check must be a key contained in the character["Skills"] dictionary
    :postcondition: determines whether or not an ability is on cooldown or not
    :return: a checkmark as a string if the ability is ready, an X as a string if the ability is
            not ready
    """
    # if ability is not ready, return x icon
    if is_on_cooldown(character, skill_to_check):
        return "❌"
    # if ability is ready, return checkmark icon
    else:
        return "✅"


def is_on_cooldown(character: dict, skill_to_check: str) -> bool:
    """
    Determine if an ability is on cooldown.

    :param character: a dictionary
    :param skill_to_check: a key in a dictionary
    :precondition: character dictionary must contain key "Skills" which contains a dictionary
                storing keys that represent other abilities which each contain a diction
                storing a key named "Cooldown" which stores a list with two integer elements
                which represent current cooldown and maximum cooldown
    :precondition: skill to check must be a key contained in the character["Skills"] dictionary
    :postcondition: determines whether or not an ability is on cooldown or not
    :return: True if the ability is not ready (on cooldown) or False if the ability is ready
    """
    if character["Skills"][skill_to_check]["Cooldown"][0] >= \
            character["Skills"][skill_to_check]["Cooldown"][1]:
        # return False if ability is ready
        return False
    # return True if ability is not ready
    return True


def print_enemy_encounter(enemy: dict, character: dict) -> None:
    """
    Print the enemy encounter.

    :param enemy: a dictionary
    :param character: a dictionary
    :precondition: enemy dictionary must contain the keys "Name" (str), "Current HP" (int),
                    "Max HP"(int), and "Appeared"(bool)
    :precondition: character dictionary must contain the keys "Level", "Current HP", and "Max HP"
    """
    if not enemy["Appeared"]:
        print(F"{enemy['Name']} appears!")
        enemy["Appeared"] = True
    print(F"\n{enemy['Name']}:\n"
          F"Enemy:  Level\t\tHealth\n"
          F"\t\t  {enemy['Level']}\t\t\t{enemy['Current HP']} / {enemy['Max HP']}\n\n"
          F"You:\tLevel\t\tHealth\n"
          F"\t\t  {character['Level']}\t\t    {character['Current HP']} / {character['Max HP']}")


def choose_fight_option() -> str:
    """
    Prompt user to select a battle choice.

    :postcondition: prompt user to fight or flee and return battle choice when user inputs a "1"
                    or "2"
    :return: "1" or "2" as a string
    """
    while True:
        battle_choice = input(F"-\tFight\t\t(1)\n"
                              F"-\tFlee\t\t(2)\n")
        if battle_choice not in ['1', '2']:
            print(F"{battle_choice} is not a valid selection. Choose 1, or 2")
        else:
            return battle_choice


def generate_enemy(character: dict) -> dict:
    """
    Generate an enemy.

    This function takes a character's location and generates an enemy that belongs there.

    :param character: a dictionary
    :precondition: character dictionary must contain keys "Y-Coordinate" and "X-Coordinate"
    :postcondition: an enemy is generated that is reflective of the area of the map the player
                    is standing in from level 1 to 3
    :return: enemy dictionary containing a monster from level 1 to 3
    """
    weak_enemies = {"Angry Duck": "pecks at you with its bill",
                    "Dirty Raccoon": "bites at your leg",
                    "Annoyed Frog": "jumps into your face",
                    "Feral Squirrel": "leaps into your face and scratches you",
                    "Irate Mouse": "leaps at your arm and bites you",
                    "Hungry Seagull": "swoops into your face and pecks you"}
    medium_enemies = {"Fierce Wolf": "bites you with sharp teeth",
                      "Irritated Bear": "gallops into your and bites your torso",
                      "Ferocious Cougar": "leaps into you and bites your torso",
                      "Enraged Alligator": "scurries into you and bites your leg",
                      "Bitter Moose": "rams you with its antlers",
                      "Hungry Hippo": "bulldozes into you with its immense weight"}
    hard_enemies = {"Undead Soldier": "slashes at you with its corrupted sword",
                    "Enraged Skeleton": "leaps at you with daggers and violently strikes",
                    "Undead Wolf": "viciously bites you with unnatural strength",
                    "Giant Spider": "pounces at you and bites your torso",
                    "Resentful Spirit": "screams at you with a deafening cry",
                    "Corrupt Wraith": "slashes at you with its ethereal scythe"}

    if area_level(character) == 1:
        generated_enemy = {"Level": 1, "Current HP": random.randint(7, 10), "Accuracy": 50,
                           "Damage": random.randint(2, 3),
                           "Experience reward": random.randint(20, 35),
                           "Name": [name for name in weak_enemies.keys()]
                           [random.randint(0, len(weak_enemies) - 1)]}
        generated_enemy.update({"Move": weak_enemies[generated_enemy["Name"]]})

    elif area_level(character) == 2:
        generated_enemy = {"Level": 2, "Current HP": random.randint(50, 75), "Accuracy": 65,
                           "Damage": random.randint(6, 9),
                           "Experience reward": random.randint(150, 200),
                           "Name": [name for name in medium_enemies.keys()]
                           [random.randint(0, len(medium_enemies) - 1)]}
        generated_enemy.update({"Move": medium_enemies[generated_enemy["Name"]]})
    else:
        generated_enemy = {"Level": 3, "Current HP": random.randint(150, 200), "Accuracy": 70,
                           "Damage": random.randint(15, 20),
                           "Experience reward": random.randint(800, 1000),
                           "Name": [name for name in hard_enemies.keys()]
                           [random.randint(0, len(hard_enemies) - 1)]}
        generated_enemy.update({"Move": hard_enemies[generated_enemy["Name"]]})
    generated_enemy.update({"Max HP": generated_enemy["Current HP"], "Appeared": False})
    return generated_enemy


def check_for_foes() -> bool:
    """
    Check for foes.

    This function rolls a weighted random choice. It will return
    a True 25% of the time and a False 75% of the time.

    :postcondition: makes a weighted random choice 25% True and 75% False
    :return: True if 25% random chance is chosen, False if 75% random chance is chosen
    """
    return random.choices([True, False], weights=[25, 75], k=1)[0]


def move_character(character: dict, direction: int):
    """
    Move the character.

    This function moves the character in the direction
    specified, regardless of if it's a valid move.

    :param character: a dictionary containing the keys "X-Coordinate" and "Y-Coordinate"
    :param direction: an integer as either 1, 2, 3, or 4 representing North, South, west and East
    :precondition: dictionary is properly formatted and contains keys X-Coordinate, and Y-Coordinate
                    with values as non-negative integers
    :precondition: direction is a valid integer of 1, 2, 3, or 4
    :postcondition: updates the character's location 1 spot into the direction where 1 is North, 2
                    is South, 3 is west, and 4 is East

    move character South (y-coordinate + 1)
    >>> character_data = {"X-Coordinate": 0, "Y-Coordinate": 0}
    >>> move_character(character_data, 2)
    >>> print(character_data)
    {'X-Coordinate': 0, 'Y-Coordinate': 1}

    move character west (x-coordinate -1)
    >>> character_data = {"X-Coordinate": 1, "Y-Coordinate": 0}
    >>> move_character(character_data, 3)
    >>> print(character_data)
    {'X-Coordinate': 0, 'Y-Coordinate': 0}
    """
    character['X-Coordinate'] = calculate_new_coords(character, direction)[0]
    character['Y-Coordinate'] = calculate_new_coords(character, direction)[1]


def validate_move(board: dict, character: dict, direction: int) -> bool:
    """
    Validate a move.

    This function determines whether or not a character's movement in the specified direction will
    place the character outside of the playable area determined by the passed in board. If the move
    is valid, this function returns True, if not, False.

    :param board: a dictionary representing the map as tuple keys representing coordinates and
                    values containing the description of the location at those coordinates in the
                    form {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (0, 2): 'Town'}
    :param character: a dictionary containing the keys for X-Coordinate, Y-Coordinate as
                        non-negative integers
    :param direction: an integer as either 1, 2, 3, or 4 representing North, South, west and East
    :precondition: dictionary contains only proper keys and values that correspond to a map in the
                    form {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (0, 2): 'Town'}, all
                    values must be non-negative integers
    :precondition: dictionary is properly formatted and contains keys X-Coordinate, and Y-Coordinate
    :precondition: direction is a valid integer of 1, 2, 3, or 4
    :postcondition: will determine whether or not the proposed move is valid. does not change
                    board or character location
    :return: True if valid, False if invalid

    an invalid move that exits the board
    >>> validate_move({(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (0, 2): 'Town'}, \
    {"X-Coordinate": 0, "Y-Coordinate": 0}, 1)
    False

    a valid move within the board
    >>> validate_move({(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (0, 2): 'Town'}, \
    {"X-Coordinate": 0, "Y-Coordinate": 0}, 2)
    True
    """
    # calls a function to calculate the suggested new coordinates
    proposed_coords = calculate_new_coords(character, direction)

    # checks to see if function exists on board
    return proposed_coords in board and board[proposed_coords] not in ["H", "V", "+"]


def calculate_new_coords(character: dict, direction: int) -> tuple:
    """
    Calculate new coordinates.

    This function takes a character dictionary and a direction integer and returns the coordinate
    that would be obtained from moving the character one space in the specified direction.

    :param character: a dictionary containing the keys for X-Coordinate, Y-Coordinate, and Current
                        HP in the form: {"X-Coordinate": 0, "Y-Coordinate": 0, "Current HP": 5}
    :param direction: an integer as either 1, 2, 3, or 4 representing North, South, west and East
    :precondition: dictionary is properly formatted and contains keys X-Coordinate, and Y-Coordinate
    :precondition: direction is a valid integer of 1, 2, 3, or 4
    :postcondition: calculates a tuple containing the new coordinates
    :return: tuple containing new coordinates

    calculate new coordinates going west
    >>> calculate_new_coords({"X-Coordinate": 1, "Y-Coordinate": 0}, 3)
    (0, 0)

    calculate new coordinates going North
    >>> calculate_new_coords({"X-Coordinate": 1, "Y-Coordinate": 0}, 1)
    (1, -1)
    """
    # maps directions from input to changes on actual coords
    direction_dictionary = {1: -1, 2: 1, 3: -1, 4: 1}
    if direction == 1 or direction == 2:
        new_coord = (character["X-Coordinate"], character["Y-Coordinate"]
                     + direction_dictionary[direction])
    else:
        new_coord = (character["X-Coordinate"] + direction_dictionary[direction],
                     character["Y-Coordinate"])

    return new_coord


def describe_current_location(board: dict, character: dict) -> None:
    """
    Print out the room the player is standing in.

    This function receives a board dictionary and a character dictionary, then prints out the spot
    that the character is standing on in relation to the passed in board.

    :param board: a dictionary representing the map as tuple keys representing coordinates and
                    values containing the description of the location at those coordinates in the
                    form {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (0, 2): 'Town'}
    :param character: a dictionary containing the keys "X-Coordinate", and "Y-Coordinate"
    :precondition: dictionary contains only proper keys and values that correspond to a board in the
                    form {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (0, 2): 'Town'}, all
                    values must be non-negative integers
    :precondition: dictionary is properly formatted and contains keys X-Coordinate, and Y-Coordinate
                    as non-negative integers that as a tuple (X-Coordinate, Y-Coordinate) exist
                    in the board as a key
    :postcondition: prints out a new line, the value in the board corresponding to the coordinates
                    the player is standing on in relation to the map and prints out the coordinates
                    afterwards

    describe the location of the character at (0, 0) on the map
    >>> describe_current_location({(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (0, 2): 'Town'},\
    {'X-Coordinate': 0, 'Y-Coordinate': 0})
    <BLANKLINE>
    0, 0
    Grassy Area

    describe the location of the character at (0, 1) on the map
    >>> describe_current_location({(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (0, 2): 'Town'},\
    {'X-Coordinate': 0, 'Y-Coordinate': 1})
    <BLANKLINE>
    0, 1
    Forested Area
    """
    if character["Y-Coordinate"] >= 17:  # Level 1 area
        room_index = {1: color_text("A peaceful grassy area. Birds are chirping and the wind "
                                    "gently blows.", [41, 156, 32]),
                      2: color_text("A peaceful flowery area. Tree leaves rustle softly.",
                                    [37, 141, 28]),
                      3: color_text("A peaceful bushy area. Small animals scurry about.",
                                    [37, 141, 28]),
                      4: color_text("A peaceful rocky area. Grass sways around the rocks.",
                                    [37, 141, 28])}
    elif character["Y-Coordinate"] >= 9:  # Level 2 area
        room_index = {1: color_text("A grassy area. The sky is cloudy and the wind is blowing "
                                    "against you.", [171, 173, 36]),
                      2: color_text("A flowery area. The flowers are restlessly shuffling with "
                                    "the wind.", [171, 173, 36]),
                      3: color_text("A bushy area. The bushes rustle loudly as the wind blows "
                                    "through them.", [171, 173, 36]),
                      4: color_text("A rocky area. The wind is strong.", [171, 173, 36])}
    else:  # Level 3 area
        room_index = {1: color_text("A dark grassy area. The sky is red and it's getting hard "
                                    "to see.", [150, 35, 35]),
                      2: color_text("A dark flowery area. The sky is red, and the flowers have "
                                    "wilted.", [150, 35, 35]),
                      3: color_text("A dark bushy area. The sky is red, and mysterious sounds can "
                                    "be heard.", [150, 35, 35]),
                      4: color_text("A dark rocky area. The sky is red, and it's very hard to "
                                    "see.", [150, 35, 35])}
    # Print the area the character is standing on.
    room_index.update({"t": F"An artifact gleams beneath your feet.",
                       "B": F"A weary light allows you a glimpse of a silhouette floating in"
                            F" mid-air.",
                       "E": F"You find a crack in the wall and squeeze through it."})

    # print the character's coordinates
    print(F"{room_index[board[(character['X-Coordinate'], character['Y-Coordinate'])]]}")


def boss_fight(character: dict) -> bool:
    """
    Facilitate a fight with the boss.

    :param character: a dictionary
    :precondition: character dictionary must contain keys "Current HP", "Max HP", "Level",
                    "Damage", "Accuracy", "X-Coordinate", "Y-Coordinate", "Skills", and
                    "Saved path"
    :precondition: key "Skills" must contain a dictionary containing at least one skill name
                    as a key, which contains a dictionary with keys "Damage Multiplier", and
                    "Cooldown" which contains a list of two elements with the first index
                    representing cooldown and the second index representing the max cooldown
    :precondition: key "Saved path" must contain a list of at least two tuples which each
                    contain two integer elements representing x and y coordinates, respectively
    :postcondition: facilitates a full fight with the boss
    :postcondition: determines whether or not the player has died or the boss has died
    :return: True if boss is dead, False if boss is alive
    """
    boss_intro(character)
    enemy = {'Level': 3,
             'Current HP': 650,
             'Accuracy': 50,
             'Damage': 30,
             'Experience reward': 1000,
             'Name': 'Necromancer',
             'Move': "Orders their summoned servants to charge into you.\n"
                     "You get stabbed, slashed and shot from various angles.",
             'Max HP': 650,
             'Appeared': False}
    while not is_dead(enemy) and not is_dead(character):
        print_enemy_encounter(enemy, character)
        selection = choose_fight_option()
        # fight is selected
        if selection == '1':
            attack_enemy(choose_attack(character), enemy, character)
            if is_dead(enemy):
                return True
            enemy_attack(enemy, character)
        elif selection == '2':
            print("You cannot run from the Necromancer")
    return False


def boss_intro(character: dict) -> None:
    """
    Print intro scene for boss encounter.

    :param character: a dictionary
    :precondition: character dictionary must contain the key "Class" with a printable value
    """
    print("The air is thick with the scent of blood.")
    time.sleep(2)
    print("As you step closer, a red mist pools ahead of you")
    time.sleep(2)
    print(F"The silhouette turns and you get a better glimpse of it.")
    time.sleep(4)
    print(F"\n\t'Hahaha,'")
    time.sleep(3)
    print(F"\n\t'I've been expecting you, {character['Class']}'\n")
    time.sleep(2)
    print(F"An enormous red aura rushes in from every corner of the room \n"
          F"into the silhouette and the room fills with red light.\n")
    time.sleep(4)
    print(F"The necromancer's giant grin startles you.")
    time.sleep(2)
    print(F"You get into combat stance.\n")


def check_for_boss(board: dict, character: dict) -> bool:
    """
    Check character's location for boss.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board dictionary must contain key tuples containing two element integers
                    representing x and y coordinates, respectively
    :precondition: character dictionary must contain keys "X-Coordinate" and "Y-Coordinate"
                    with values as integers, which when combined into a tuple of (x, y) should
                    should exist as a key in the board dictionary
    :return: True if character is standing on the boss tile, False if not

    check a spot where the boss exists
    >>> check_for_boss({(0, 0): "B"}, {"X-Coordinate": 0, "Y-Coordinate": 0})
    True

    check a spot where the boss doesn't exist
    >>> check_for_boss({(0, 0): "B", (1, 0): "C"}, {"X-Coordinate": 1, "Y-Coordinate": 0})
    False
    """
    if board[(character["X-Coordinate"], character["Y-Coordinate"])] == "B":
        return True
    else:
        return False


def check_for_treasure(board: dict, character: dict):
    """
    Check for treasure and remove it from the board.

    :param board: a dictionary
    :param character: a dictionary
    :precondition: board dictionary must contain key tuples containing two element integers
                    representing x and y coordinates, respectively
    :postcondition: character dictionary must contain keys "X-Coordinate" and "Y-Coordinate"
                    with values as integers, which when combined into a tuple of (x, y) should
                    should exist as a key in the board dictionary
    :return:
    check a spot where the boss exists
    >>> board_example = {(0, 0): "t"}
    >>> character_example = {"X-Coordinate": 0, "Y-Coordinate": 0}
    >>> check_for_treasure(board_example, character_example)
    True

    # check if "t" was removed from map
    >>> board_example != {(0, 0): "t"}
    True
    """
    if board[(character["X-Coordinate"], character["Y-Coordinate"])] in ["t", "T"]:
        remove_symbol_from_map(character, board)
        return True
    else:
        return False


def remove_symbol_from_map(character: dict, board: dict) -> None:
    """
    Replace a symbol from a board with an integer from 1 to 4.

    :param character: a dictionary
    :param board: a dictionary
    :precondition: character dictionary must contain the keys "X-Coordinate" and "Y-Coordinate"
                    each containing an integer and when combined into a tuple, match a key from the
                    board
    :precondition: board dictionary must contain key tuples containing two element integers
                    representing x and y coordinates, respectively
    """
    # replace character's position on map with a number 1 through 4
    board[(character["X-Coordinate"], character["Y-Coordinate"])] = random.randint(1, 4)


def check_for_exit(character: dict, board: dict) -> bool:
    """
    Check for an exit and move the character if found.

    :param character: a dictionary
    :param board: a dictionary
    :precondition: character dictionary must contain the keys "X-Coordinate" and "Y-Coordinate" each
                    containing an integer
    :precondition: board dictionary must contain key tuples containing two element integers
                    representing x and y coordinates, respectively, and must include the tuple
                    containing the character's X-Coordinate and Y-Coordinate and the tuple that
                    represents the character's Y-Coordinate plus two.
    :postcondition: detects whether or not the character is standing on an exit
    :postcondition: moves the character's Y-Coordinate plus two if they have encountered an exit
    :return: a boolean representing whether or not the player has found an exit

    # check that a player that is standing on an exit
    >>> character_example = {"X-Coordinate": 0, "Y-Coordinate": 0}
    >>> board_example = {(0, 0): "E", (0, 2): "1"}
    >>> check_for_exit(character_example, board_example)
    True

    # check that the player has been moved
    >>> print(character_example)
    {'X-Coordinate': 0, 'Y-Coordinate': 2}
    """
    if board[character["X-Coordinate"], character["Y-Coordinate"]] == "E":
        character["Y-Coordinate"] += 2
        return True
    return False


def pick_up_treasure(character: dict) -> None:
    """
    Pick up a treasure off the map.

    :param character: a dictionary
    :precondition: character dictionary must include keys "Max HP", "Current HP", and "Damage",
                    each of which contain an integer valuee
    :postcondition: generates a treasure with a random name and buff and modifies the character's
                    dictionary to reflect the modification
    """
    treasure_value = random.randint(1, 5)
    treasure_name = identify_treasure(treasure_value)
    buff_choice = random.randint(1, 3)
    if buff_choice == 1:
        print(F"Artifact: {treasure_name}\n"
              F"You gain {treasure_value} max health!")
        character["Max HP"] += treasure_value

    elif buff_choice == 2:
        print(F"Artifact: {treasure_name}\n"
              F"You gain {treasure_value * .5} damage!")
        character["Damage"] += treasure_value * .5

    elif buff_choice == 3:
        print(F"Artifact: {treasure_name}\n"
              F"You heal back to max health!")
        character["Current HP"] = character["Max HP"]


def identify_treasure(treasure_value) -> str:
    """
    Identify treasure.

    This function accepts an integer from 1 to 5 indicating quality and generates a randomly
    named treasure containing a word, indicative of the quality of the buff.

    :param treasure_value: an integer
    :precondition: treasure_value integer must be an integer from 1 to 5 inclusive
    :postcondition: generates a treasure name using the treasure value
    :return: treasure name as a string
    """
    treasure_adjective = ["Dusty", "Shiny", "Excellent", "Exquisite", "Ancient"]
    treasure_base_names = ["Lamp", "Coin", "Medallion", "Bracelet", "Glove", "Branch"]
    treasure_second_names = ["Corruption", "Content", "Earth-breaking", "Scarlet-Guardian",
                             "Anger", "Brute", "Skill", "Delinquent"]

    treasure_name = F"{treasure_adjective[treasure_value - 1]} " \
                    F"{treasure_base_names[random.randint(0, len(treasure_base_names) - 1)]} of " \
                    F"{treasure_second_names[random.randint(0, len(treasure_second_names) - 1)]}"

    return treasure_name


def get_user_choice() -> int:
    """
    Get direction to move from player.

    This function prompts the user to type a direction corresponding to a number. The player will
    continue to be prompted until they input an accepted number

    :postcondition: asks the user which direction to go and maps it to integer 1 for North, 2 for
                    South, 3 for West, or 4 for East
    :return: integer 1 for North, 2 for South, 3 for West, or 4 for East
    """
    choice_to_int = {'W': 1, 'S': 2, 'A': 3, 'D': 4, "P": 5, "QUIT": "QUIT"}
    while True:
        chosen_direction = input("Which direction would you like to go?\n"
                                 "North (W), West (A), South (S), East (D)\n"
                                 "Status(P), Quit(quit)")
        if chosen_direction.upper() not in ['W', 'A', 'S', 'D', 'P', 'QUIT']:
            print(F"{chosen_direction} is not valid. You must input a W, A, S, or D")
        # Display character status
        else:
            return choice_to_int[chosen_direction.upper()]


def game():
    """
    Loop game.
    """
    character = {}
    intro_sequence()
    ask_for_name(character)
    board = create_initial_board()
    create_character(character)
    print_scenario(character)
    achieved_goal = False
    while not achieved_goal and not is_dead(character):
        # Tell the user where they are
        print_map_location_character(board, character)
        if check_for_treasure(board, character):
            pick_up_treasure(character)
        if check_for_boss(board, character):
            achieved_goal = boss_fight(character)
            continue
        if check_for_exit(character, board):
            continue
        direction = get_user_choice()
        # Show Character status or open inventory
        if direction == 5:
            show_status(character)
            continue
        if direction == "QUIT":
            break
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            save_path(character)
            # 25% chance to encounter a foe
            there_is_a_challenger = check_for_foes()
            print_map_location_character(board, character)
            if there_is_a_challenger:
                clear_console()
                combat_game(character)
                prompt_to_continue()
            clear_console()
        else:
            clear_console()
            print("You can't go in that direction")
            continue
        reduce_cooldown_heal(character)

    if is_dead(character):
        print("Nice job, you died")
    elif achieved_goal:
        ending_sequence(character)
    print(F"\nThanks for playing, {character['Name']}")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
