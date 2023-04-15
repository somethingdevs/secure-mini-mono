import random


def dice_roll():
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    total_dice = first_dice + second_dice
    if first_dice == second_dice:
        print(f'x rolled doubles of {first_dice}!')  # Change player name
    print(f'x rolled {total_dice}')  # Change player name
    return total_dice


BOARD_TILES_NO = 32
BOARD_TILES = ["Start/GO",
               "Goa",
               "Income Tax",
               "Pondicherry",
               "Secunderabad Station",
               "Rishikesh",
               "Nainital",
               "Gulmarg",
               "Visiting Jail/Jail",
               "Udaipur",
               "Raipur",
               "Darjeeling",
               "Chennai Central Station",
               "Vijayawada",
               "Wayanad",
               "Mysore",
               "Free Parking",
               "Gangtok",
               "Ahmedabad",
               "Lucknow",
               "Chatrapathi Shivaji Terminal Station",
               "Jaipur",
               "Bhopal",
               "Kochi",
               "GO TO JAIL",
               "Bangalore",
               "Hyderabad",
               "Kolkata",
               "Howrah Station",
               "Delhi",
               "Luxury Tax",
               "Mumbai"]