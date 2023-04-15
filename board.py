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
# BOARD_TILES = {"Start/GO",
#                "Goa",
#                "Income Tax",
#                "Pondicherry",
#                "Secunderabad Station",
#                "Rishikesh",
#                "Nainital",
#                "Gulmarg",
#                "Visiting Jail/Jail",
#                "Udaipur",
#                "Raipur",
#                "Darjeeling",
#                "Chennai Central Station",
#                "Vijayawada",
#                "Wayanad",
#                "Mysore",
#                "Free Parking",
#                "Gangtok",
#                "Ahmedabad",
#                "Lucknow",
#                "Chatrapathi Shivaji Terminal Station",
#                "Jaipur",
#                "Bhopal",
#                "Kochi",
#                "GO TO JAIL",
#                "Bangalore",
#                "Hyderabad",
#                "Kolkata",
#                "Howrah Station",
#                "Delhi",
#                "Luxury Tax",
#                "Mumbai"}

# Dictionary looking ass
# {key : value}
# {tile_name : description, color, price, mortage_value, [rent with 0 houses, rent with 1 house, rent with 2 houses, rent with hotel], house_building_cost, hotel_building_cost}

BOARD_TILES_INFO = {
    "Start/GO": ["Collect $200 salary as you pass GO", None, None, None, [None, None, None, None], None, None],
    "Goa": ["This beautiful coastal state is known for its beaches, nightlife and Portuguese architecture.", "brown", 60, 30, [2, 10, 30, 90, 160, 250], 50, 50],
    "Income Tax": ["Pay 10% of your total worth or $200, whichever is lesser.", None, None, None, [None, None, None, None], None, None],
    "Pondicherry": ["This Union Territory is known for its French architecture and quaint cafes.", "brown", 60, 30, [4, 20, 60, 180, 320, 450], 50, 50],
    "Railway1: Secundarabad Station": ["This railway station connects Hyderabad to various parts of the country.", "black", 200, 100, [25, 50, 100, 200], None, None],
    "Rishikesh": ["This holy city is known for its beautiful temples and as a hub for adventure sports like river rafting.", "light blue", 100, 50, [6, 30, 90, 270, 400, 550], 50, 50],
    "Nainital": ["This hill station is known for its scenic beauty and is a popular tourist destination.", "light blue", 100, 50, [6, 30, 90, 270, 400, 550], 50, 50],
    "Gulmarg": ["This ski resort in Jammu & Kashmir is known for its picturesque landscapes and winter sports.", "light blue", 120, 60, [8, 40, 100, 300, 450, 600], 50, 50],
    "Visiting Jail": ["Just visiting", None, None, None, [None, None, None, None], None, None],
    "Udaipur": ["This city in Rajasthan is known for its beautiful lakes, palaces and museums.", "pink", 140, 70, [10, 50, 150, 450, 625, 750], 100, 100],
    "Raipur": ["This city in Chhattisgarh is known for its rich cultural heritage and is a commercial hub.", "pink", 140, 70, [10, 50, 150, 450, 625, 750], 100, 100],
    "Darjeeling": ["This hill station in West Bengal is known for its tea plantations and scenic views of the Himalayas.", "pink", 160, 80, [12, 60, 180, 500, 700, 900], 100, 100],
    "Railway4: Chennai Central Station": ["This railway station is one of the busiest in the country and connects Chennai to various parts of India.", "black", 200, 100, [25, 50, 100, 200], None, None],
    "Vijayawada": ["This city in Andhra Pradesh is known for its rich history, cultural heritage and scenic beauty.", "orange", 180, 90, [14, 70, 200, 550, 750, 950], 100, 100],
    "Waynad": ["Orange", 180, 90, [14, 70, 200, 550, 750, 950], 100, 100],
    "Mysore": ["Orange", 200, 100, [16, 80, 220, 600, 800, 1000], 100, 100],
    "Free Parking": ["N/A", 0, 0, [0, 0, 0, 0, 0, 0], 0, 0],
    "Gangtok": ["Red", 220, 110, [18, 90, 250, 700, 875, 1050], 150, 150],
    "Ahmedabad": ["Red", 220, 110, [18, 90, 250, 700, 875, 1050], 150, 150],
    "Lucknow": ["Red", 240, 120, [20, 100, 300, 750, 925, 1100], 150, 150],
    "Chatrapathi Shivaji Terminal Station": ["Railway", 200, 100, [25, 50, 100, 200], 0, 0],
    "Jaipur": ["Yellow", 260, 130, [22, 110, 330, 800, 975, 1150], 150, 150],
    "Bhopal": ["Yellow", 260, 130, [22, 110, 330, 800, 975, 1150], 150, 150],
    "Kochi": ["Yellow", 280, 140, [24, 120, 360, 850, 1025, 1200], 150, 150],
    "GO TO JAIL": ["N/A", 0, 0, [0, 0, 0, 0, 0, 0], 0, 0],
    "Bangalore": ["Green", 300, 150, [26, 130, 390, 900, 1100, 1275], 200, 200],
    "Hyderabad": ["Green", 300, 150, [26, 130, 390, 900, 1100, 1275], 200, 200],
    "Kolkata": ["Green", 320, 160, [28, 150, 450, 1000, 1200, 1400], 200, 200],
    "Howrah Station": ["Railway", 200, 100, [25, 50, 100, 200], 0, 0],
    "Delhi": ["Dark Blue", 350, 175, [35, 175, 500, 1100, 1300, 1500], 200, 200],
    "Luxury Tax": ["N/A", 0, 0, [0, 0, 0, 0, 0, 0], 0, 0],
    "Mumbai": ["Dark Blue", 400, 200, [50, 200, 600, 1400, 1700, 2000], 200, 200]
}




