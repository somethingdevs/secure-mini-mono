-- MAYBE MAKE A ER DIAGRAM IF TIME PERMITS?

CREATE TABLE user(
user_id INT PRIMARY KEY,
username VARCHAR(20),
email VARCHAR(40),
pass VARCHAR(40)
);

CREATE TABLE room(
room_id INT PRIMARY KEY,
room_player INT,
room_status VARCHAR(10),
room_winner INT,
FOREIGN KEY(room_player) REFERENCES user(user_id),
FOREIGN KEY(room_winner) REFERENCES user(user_id)
);

CREATE TABLE property_list(
    property_id INT PRIMARY KEY,
    property_name VARCHAR(50),
    property_description VARCHAR(455),
    property_cost INT,
    property_rent INT,
    property_house_cost INT,
    property_hotel_cost INT,
    is_property_special BOOL
);


CREATE TABLE logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    log_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    log_value VARCHAR(255)
);


CREATE TABLE player_property (
    room_id INT,
    player_id INT,
    property_id INT,
    PRIMARY KEY (room_id, player_id, property_id),
    FOREIGN KEY (room_id) REFERENCES room(room_id),
    FOREIGN KEY (player_id) REFERENCES player(player_id),
    FOREIGN KEY (property_id) REFERENCES property_list(player_prop_id)
    );
    
CREATE TABLE player (
    room_id INT,
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    player_balance INT,
    player_prop_id INT,
    player_position INT,
    player_round INT,
    FOREIGN KEY (player_prop_id) REFERENCES player_property(property_id),
    FOREIGN KEY (room_id) REFERENCES room(room_id)
    );
    

    
    
query_list = [
    "INSERT INTO property_list VALUES(0, 'Start/GO', 'Collect $200 salary as you pass GO', NULL, NULL, NULL, NULL, FALSE)",
    "INSERT INTO property_list VALUES(1, 'Goa', 'This beautiful coastal state is known for its beaches, nightlife and Portuguese architecture.', 60, 2, 50, 50, FALSE)",
    "INSERT INTO property_list VALUES(2, 'Income Tax', 'Pay 10% of your total worth or $200, whichever is lesser.', NULL, NULL, NULL, NULL, FALSE)",
    "INSERT INTO property_list VALUES(3, 'Pondicherry', 'This Union Territory is known for its French architecture and quaint cafes.', 60, 4, 50, 50, FALSE)",
    "INSERT INTO property_list VALUES(4, 'Railway1: Secundarabad Station', 'This railway station connects Hyderabad to various parts of the country.', 200, 25, NULL, NULL, FALSE)",
    "INSERT INTO property_list VALUES(5, 'Rishikesh', 'This holy city is known for its beautiful temples and as a hub for adventure sports like river rafting.', 100, 6, 50, 50, FALSE)",
    "INSERT INTO property_list VALUES(6, 'Nainital', 'This hill station is known for its scenic beauty and is a popular tourist destination.', 100, 6, 50, 50, FALSE)",
    "INSERT INTO property_list VALUES(7, 'Gulmarg', 'This ski resort in Jammu & Kashmir is known for its picturesque landscapes and winter sports.', 120, 8, 50, 50, FALSE)",
    "INSERT INTO property_list VALUES(8, 'Udaipur', 'This city in Rajasthan is known for its beautiful lakes, palaces and museums.', 140, 10, 100, 100, FALSE)",
    "INSERT INTO property_list VALUES(9, 'Visiting Jail', 'Just visiting', NULL, NULL, NULL, NULL, TRUE)",
    "INSERT INTO property_list VALUES(10, 'Raipur', 'This city in Chhattisgarh is known for its rich cultural heritage and is a commercial hub.', 140, 10, 100, 100, FALSE)",
    "INSERT INTO property_list VALUES(11, 'Darjeeling', 'This hill station in West Bengal is known for its tea plantations and scenic views of the Himalayas.', 160, 12, 100, 100, FALSE)",
    "INSERT INTO property_list VALUES(12, 'Railway2: Chennai Central Station', 'This railway station is one of the busiest in the country and connects Chennai to various parts of India.', 200, 25, NULL, NULL, FALSE)",
    "INSERT INTO property_list VALUES(13, 'Vijayawada', 'This city in Andhra Pradesh is known for its rich history, cultural heritage and scenic beauty.', 180, 14, 100, 100, FALSE)",
    "INSERT INTO property_list VALUES(14, 'Waynad', 'A scenic hill station located in the Western Ghats of Kerala known for its lush green forests, misty valleys, and wildlife.', 180, 14, 100, 100, FALSE)",
    "INSERT INTO property_list VALUES(15, 'Mysore', 'A city in the state of Karnataka known for its rich cultural heritage, palaces, and vibrant festivals such as Dasara.', 200, 16, 100, 100, FALSE)",
    "INSERT INTO property_list VALUES(16, 'Free Parking', 'A space on the board where players can park for free without any penalty.', NULL, NULL, NULL, NULL, TRUE)",
    "INSERT INTO property_list VALUES(17, 'Gangtok', 'The capital city of Sikkim known for its panoramic views of the Himalayas, Buddhist monasteries, and adventurous activities such as trekking and river rafting.', 220, 18, 150, 150, FALSE)",
    "INSERT INTO property_list VALUES(18, 'Ahmedabad', 'A city in the state of Gujarat known for its rich history, cultural heritage, and the Sabarmati Ashram, the former residence of Mahatma Gandhi.', 220, 18, 150, 150, FALSE)",
    "INSERT INTO property_list VALUES(19, 'Lucknow', 'A city in the state of Uttar Pradesh known for its Nawabi culture, cuisine, and the grandiose Bara Imambara and Chhota Imambara.', 240, 20, 150, 150, FALSE)",
    "INSERT INTO property_list VALUES(20, 'Railway3: Chatrapathi Shivaji Terminal Station', 'A railway station in Mumbai, Maharashtra known for its impressive Victorian Gothic architecture and being one of the busiest railway stations in India.', 200, 25, NULL, NULL, FALSE)",
    "INSERT INTO property_list VALUES(21, 'Jaipur', 'The capital city of Rajasthan known for its grandiose palaces, forts, and colorful markets.', 260, 22, 150, 150, FALSE)",
    "INSERT INTO property_list VALUES(22, 'Bhopal' , 'The capital city of Madhya Pradesh known for its beautiful lakes, national parks, and museums.', 260, 22, 150, 150, FALSE)",
    "INSERT INTO property_list VALUES(23, 'Kochi' , 'A city in the state of Kerala known for its backwaters, beaches, and historic landmarks such as the Mattancherry Palace and Jewish Synagogue.', 280, 24, 150, 150, FALSE)",
    "INSERT INTO property_list VALUES(24, 'GO TO JAIL','A space on the board that represents being sent to jail if a player lands on it.', NULL, NULL, NULL, NULL, TRUE)",
    "INSERT INTO property_list VALUES(25, 'Bangalore', 'The capital city of Karnataka known for its technology parks, nightlife, and beautiful parks such as the Lalbagh Botanical Garden.', 300, 26, 200, 200, FALSE)",
    "INSERT INTO property_list VALUES(26, 'Hyderabad','The capital city of Telangana known for its rich history, cuisine, and the famous Charminar monument.', 300, 26, 200, 200, FALSE)",
    "INSERT INTO property_list VALUES(27, 'Kolkata','The capital city of West Bengal known for its colonial architecture, literary culture, and delicious street food.', 320, 28, 200, 200, FALSE)",
    "INSERT INTO property_list VALUES(28, 'Railway4: Howrah Station','A railway station in Kolkata, West Bengal known for being one of the largest and busiest railway stations in India.', 200, 25, NULL, NULL, FALSE)",
    "INSERT INTO property_list VALUES(29, 'Delhi','The capital city of India known for its history, culture, and landmarks such as the Red Fort, Qutub Minar, and India Gate.', 350, 35, 200, 200, FALSE)",
    "INSERT INTO property_list VALUES(30, 'Luxury Tax','A space on the board where players must pay a luxury tax.', NULL, NULL, NULL, NULL, TRUE)",
    "INSERT INTO property_list VALUES(31, 'Mumbai', 'The financial capital of India known for its vibrant culture, Bollywood film industry, and landmarks such as the Gateway of India and Marine Drive.', 400, 50, 200, 200, FALSE)"
]



INSERT INTO user VALUES (1 , 'ali', 'deez@nuts.com', 'ali_password');
INSERT INTO user VALUES (2 , 'poorvi', 'poorv@nuts.com', 'poorvi_password');
INSERT INTO user VALUES (3 , 'deep', 'deep@nuts.com', 'deep_password');
INSERT INTO user VALUES (4, 'joe', 'joe@mama.com', 'joe_password');

select * from user;

ALTER TABLE room
DROP PRIMARY KEY,
ADD PRIMARY KEY (room_id, room_player);


INSERT INTO room VALUES(1, 1, 'ACTIVE', NULL);
INSERT INTO room VALUES(1, 2, 'ACTIVE', NULL);
INSERT INTO room VALUES(1, 3, 'ACTIVE', NULL);

select * from room;

ALTER TABLE player_property
ADD FOREIGN KEY (room_id) REFERENCES room(room_id);

ALTER TABLE player_property
ADD FOREIGN KEY (player_id) REFERENCES player(player_id);

ALTER TABLE player_property
ADD FOREIGN KEY (property_id) REFERENCES property_list(property_id);

ALTER TABLE player
ADD FOREIGN KEY (room_id) REFERENCES room(room_id);

ALTER TABLE player
ADD FOREIGN KEY (player_prop_id) REFERENCES player_property(property_id);

ALTER TABLE user
ADD FOREIGN KEY (user_id) REFERENCES player(player_id);

SELECT * FROM PLAYER;

INSERT INTO player (room_id, player_id) VALUES (1,1);
INSERT INTO player (room_id, player_id) VALUES (1,2);
INSERT INTO player (room_id, player_id) VALUES (1,3);
INSERT INTO player (room_id, player_id) VALUES (1,4);

SELECT * FROM LOGS;
SELECT * FROM PLAYER;
SELECT * FROM PLAYER_PROPERTY;
SELECT * FROM PROPERTY_LIST;
SELECT * FROM ROOM;
SELECT * FROM USER;

SELECT * FROM USER WHERE USER_ID = 
(
SELECT PLAYER_ID FROM PLAYER WHERE
ROOM_ID = 1
);

SELECT PLAYER_ID FROM PLAYER WHERE ROOM_ID = 1;

SELECT u.username FROM user u JOIN player p ON u.user_id = p.player_id WHERE p.room_id = 1;

DESCRIBE PLAYER






