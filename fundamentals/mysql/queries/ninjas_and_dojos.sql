-- Query: Create 3 new dojos
INSERT INTO dojos (name)
VALUES ("San Jose"), ("Burbank"), ("Chicago");

-- Query: Delete the 3 dojos you just created
DELETE FROM dojos WHERE id < 4;

-- Query: Create 3 more dojos
INSERT INTO dojos (name)
VALUES ("Online"), ("Home"), ("Starbucks");

-- Query: Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Corey", "Hall", 25, 7), ("Jordan", "Wade", 23, 7), ("Dirty", "Dizzle", 26, 7);

-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("Cree", "Ball", 25, 8), ("J", "Pup", 23, 8), ("Dev", "Diz", 26, 8);

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ("C", "B", 25, 9), ("J", "P", 23, 9), ("D", "D", 26, 9);

-- Query: Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas WHERE dojo_id = 7;

-- Query: Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas WHERE dojo_id = 9;

-- Query: Retrieve the last ninja's dojo
SELECT dojo_id FROM ninjas WHERE id = 9;

