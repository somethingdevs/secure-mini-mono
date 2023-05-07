# Global variables


# models board:
#     testVar = 20

moves = {
    "Roll dice": "r",
    "Build a house": "h",
    "Build a hotel": "f",
    "View assets owned": "v",
    "Sell property": "s",
    "End turn": "x"
}

BOARD_TILES_NUMBER = 32
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

BOARD_TILES = {0: 'Start/GO', 1: 'Goa', 2: 'Income Tax', 3: 'Pondicherry', 4: 'Railway1: Secundarabad Station',
               5: 'Rishikesh', 6: 'Nainital', 7: 'Gulmarg', 8: 'Visiting Jail', 9: 'Udaipur', 10: 'Raipur',
               11: 'Darjeeling', 12: 'Railway2: Chennai Central Station', 13: 'Vijayawada', 14: 'Waynad', 15: 'Mysore',
               16: 'Free Parking', 17: 'Gangtok', 18: 'Ahmedabad', 19: 'Lucknow',
               20: 'Railway3: Chatrapathi Shivaji Terminal Station', 21: 'Jaipur', 22: 'Bhopal', 23: 'Kochi',
               24: 'GO TO JAIL', 25: 'Bangalore', 26: 'Hyderabad', 27: 'Kolkata', 28: 'Railway4: Howrah Station',
               29: 'Delhi', 30: 'Luxury Tax', 31: 'Mumbai'}

# Dictionary looking ass
# {key : value}
# {tile_name : description, color, price, mortage_value, [rent with 0 houses, rent with 1 house, rent with 2 houses, rent with hotel], house_building_cost, hotel_building_cost, owned}

BOARD_TILES_INFO = {
    "Start/GO": ["Collect $200 salary as you pass GO", None, None, None, [0, 0, 0, 0], None, None, None],
    "Goa": ["This beautiful coastal state is known for its beaches, nightlife and Portuguese architecture.", "brown",
            60, 30, [2, 10, 30, 90], 50, 50, False],
    "Income Tax": ["Pay 10% of your total worth or $200, whichever is lesser.", None, None, None, [0, 0, 0, 0], None,
                   None, None],
    "Pondicherry": ["This Union Territory is known for its French architecture and quaint cafes.", "brown", 60, 30,
                    [4, 20, 60, 180], 50, 50, False],
    "Railway1: Secundarabad Station": ["This railway station connects Hyderabad to various parts of the country.",
                                       "black", 200, 100, [25, 50, 100, 200], None, None, False],
    "Rishikesh": [
        "This holy city is known for its beautiful temples and as a hub for adventure sports like river rafting.",
        "light blue", 100, 50, [6, 30, 90, 270], 50, 50, False],
    "Nainital": ["This hill station is known for its scenic beauty and is a popular tourist destination.", "light blue",
                 100, 50, [6, 30, 90, 270], 50, 50, False],
    "Gulmarg": ["This ski resort in Jammu & Kashmir is known for its picturesque landscapes and winter sports.",
                "light blue", 120, 60, [8, 40, 100, 300], 50, 50, False],
    "Visiting Jail": ["Just visiting", None, None, None, [0, 0, 0, 0], None, None, False],
    "Udaipur": ["This city in Rajasthan is known for its beautiful lakes, palaces and museums.", "pink", 140, 70,
                [10, 50, 150, 450], 100, 100, False],
    "Raipur": ["This city in Chhattisgarh is known for its rich cultural heritage and is a commercial hub.", "pink",
               140, 70, [10, 50, 150, 450], 100, 100, False],
    "Darjeeling": [
        "This hill station in West Bengal is known for its tea plantations and scenic views of the Himalayas.", "pink",
        160, 80, [12, 60, 180, 500], 100, 100, False],
    "Railway2: Chennai Central Station": [
        "This railway station is one of the busiest in the country and connects Chennai to various parts of India.",
        "black", 200, 100, [25, 50, 100, 200], None, None, False],
    "Vijayawada": ["This city in Andhra Pradesh is known for its rich history, cultural heritage and scenic beauty.",
                   "orange", 180, 90, [14, 70, 200, 550], 100, 100, False],
    "Waynad": [
        " A scenic hill station located in the Western Ghats of Kerala known for its lush green forests, misty valleys, and wildlife.",
        "Orange", 180, 90, [14, 70, 200, 550], 100, 100, False],
    "Mysore": [
        "A city in the state of Karnataka known for its rich cultural heritage, palaces, and vibrant festivals such as Dasara.",
        "Orange", 200, 100, [16, 80, 220, 600], 100, 100, False],
    "Free Parking": ["A space on the board where players can park for free without any penalty.", "N/A", None, None,
                     [0, 0, 0, 0], 0, 0, None],
    "Gangtok": [
        "The capital city of Sikkim known for its panoramic views of the Himalayas, Buddhist monasteries, and adventurous activities such as trekking and river rafting.",
        "Red", 220, 110, [18, 90, 250, 700], 150, 150, False],
    "Ahmedabad": [
        "A city in the state of Gujarat known for its rich history, cultural heritage, and the Sabarmati Ashram, the former residence of Mahatma Gandhi.",
        "Red", 220, 110, [18, 90, 250, 700], 150, 150, False],
    "Lucknow": [
        "A city in the state of Uttar Pradesh known for its Nawabi culture, cuisine, and the grandiose Bara Imambara and Chhota Imambara.",
        "Red", 240, 120, [20, 100, 300, 750], 150, 150, False],
    "Railway3: Chatrapathi Shivaji Terminal Station": [
        "A railway station in Mumbai, Maharashtra known for its impressive Victorian Gothic architecture and being one of the busiest railway stations in India.",
        "Railway", 200, 100, [25, 50, 100, 200], None, None, False],
    "Jaipur": ["The capital city of Rajasthan known for its grandiose palaces, forts, and colorful markets.", "Yellow",
               260, 130, [22, 110, 330, 800], 150, 150, False],
    "Bhopal": ["The capital city of Madhya Pradesh known for its beautiful lakes, national parks, and museums.",
               "Yellow", 260, 130, [22, 110, 330, 800], 150, 150, False],
    "Kochi": [
        "A city in the state of Kerala known for its backwaters, beaches, and historic landmarks such as the Mattancherry Palace and Jewish Synagogue.",
        "Yellow", 280, 140, [24, 120, 360, 850], 150, 150, False],
    "GO TO JAIL": ["A space on the board that represents being sent to jail if a player lands on it.", "N/A", None,
                   None, [0, 0, 0, 0], 0, 0, None],
    "Bangalore": [
        "The capital city of Karnataka known for its technology parks, nightlife, and beautiful parks such as the Lalbagh Botanical Garden.",
        "Green", 300, 150, [26, 130, 390, 900], 200, 200, False],
    "Hyderabad": [
        " The capital city of Telangana known for its rich history, cuisine, and the famous Charminar monument.",
        "Green", 300, 150, [26, 130, 390, 900], 200, 200, False],
    "Kolkata": [
        " The capital city of West Bengal known for its colonial architecture, literary culture, and delicious street food.",
        "Green", 320, 160, [28, 150, 450, 1000], 200, 200, False],
    "Railway4: Howrah Station": [
        "A railway station in Kolkata, West Bengal known for being one of the largest and busiest railway stations in India.",
        "Railway", 200, 100, [25, 50, 100, 200], None, None, False],
    "Delhi": [
        "The capital city of India known for its history, culture, and landmarks such as the Red Fort, Qutub Minar, and India Gate.",
        "Dark Blue", 350, 175, [35, 175, 500, 1100], 200, 200, False],
    "Luxury Tax": [" A space on the board where players must pay a luxury tax.", "N/A", None, None, [0, 0, 0, 0], 0, 0,
                   None],
    "Mumbai": [
        "The financial capital of India known for its vibrant culture, Bollywood film industry, and landmarks such as the Gateway of India and Marine Drive.",
        "Dark Blue", 400, 200, [50, 200, 600, 1400], 200, 200, False]
}


# Moves list, change this to display on the web page

# display_moves()

# print(BOARD_TILES_INFO['Start/GO'])
# for i in BOARD_TILES_INFO:
#     print(i)
#     print(BOARD_TILES_INFO[i])
