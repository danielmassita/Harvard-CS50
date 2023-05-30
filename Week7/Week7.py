# Harvard CS50
# https://cs50.harvard.edu/x/2023/

# Week 7 SQL
# https://cs50.harvard.edu/x/2023/weeks/7/
# tags: SQL: Tables; Types; Statements; Constraints; Indexes; Keywords, Functions; Transactions. Race Conditionals. SQL Injection Attacks.

"""
Lecture 7
Welcome!
Flat-File Database
Relational Databases
IMDb
JOINs
Indexes
Using SQL in Python
Race Conditions
SQL Injection Attacks
Summing Up
"""



"""
Welcome!
In previous weeks, we introduced you to Python, a high-level programming language that utilized the same building blocks we learned in C.
This week, we will be continuing more syntax related to Python.
Further, we will be integrating this knowledge with data.
Finally, we will be discussing SQL or Structured Query Language.
Overall, one of the goals of this course is to learn to program generally – not simply how to program in the languages described in this course.
"""



"""
Flat-File Database
As you have likely seen before, data can often be described in patterns of columns and tables.
Spreadsheets like those created in Microsoft Excel and Google Sheets can be outputted to a csv or comma-separated values file.
If you look at a csv file, you’ll notice that the file is flat in that all of our data is stored in a single table represented by a text file. We call this form of data a flat-file database.
Python comes with native support for csv files.
In your terminal window, type code favorites.py and write code as follows:
""" 
# Prints all favorites in CSV using csv.reader

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create reader
    reader = csv.reader(file)

    # Skip header row
    next(reader)

    # Iterate over CSV file, printing each favorite
    for row in reader:
        print(row[1])

# Notice that the csv library is imported. Further, we created a reader that will hold the result of csv.reader(file). The csv.reader function reads each row from the file, and in our code we store the results in reader. print(row[1]), therefore, will print the language from the favorites.csv file.
# You can improve your code as follows:

# Stores favorite in a variable

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create reader
    reader = csv.reader(file)

    # Skip header row
    next(reader)

    # Iterate over CSV file, printing each favorite
    for row in reader:
        favorite = row[1]
        print(favorite)

# Notice that favorite is stored and then printed. Also notice that we use the next function to skip to the next line of our reader.
# Python also allows you to index by the keys of a list. Modify your code as follows:
# Prints all favorites in CSV using csv.DictReader

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file, printing each favorite
    for row in reader:
        print(row["language"])

# Notice that this example directly utilizes the language key in the print statement.
# To count the number of favorite languages expressed in the csv file, we can do the following:
# Counts favorites using variables

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    scratch, c, python = 0, 0, 0

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite == "Scratch":
            scratch += 1
        elif favorite == "C":
            c += 1
        elif favorite == "Python":
            python += 1

# Print counts
print(f"Scratch: {scratch}")
print(f"C: {c}")
print(f"Python: {python}")

#Notice that each language is counted using if statements.
# Python allows us to use a dictionary to count the counts of each language. Consider the following improvement upon our code:
# Counts favorites using dictionary

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts
for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")

# Notice that the value in counts with the key favorite is incremented when it exists already. If it does not exist, we define counts[favorite] and set it to 1. Further, the formatted string has been improved to present the counts[favorite].
# Python also allows sorting counts. Improve your code as follows:
# Sorts favorites by key

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts
for favorite in sorted(counts):
    print(f"{favorite}: {counts[favorite]}")

# Notice the sorted(counts) at the bottom of the code.
# If you look at the parameters for the sorted function in the Python documentation, you will find it has many built-in parameters. You can leverage some of these built-in parameters as follows:
# Sorts favorites by value

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

def get_value(language):
    return counts[language]

# Print counts
for favorite in sorted(counts, key=get_value, reverse=True):
    print(f"{favorite}: {counts[favorite]}")

# Notice that a function called get_value is created, and that the function itself is passed in as an argument to the sorted function. The key argument allows you to tell Python the method you wish to use to sort items.
# Python has a unique ability that we have not seen to date: It allows for the utilization of anonymous or lambda functions. These functions can be utilized when you want to not bother creating an entirely different function. Notice the following modification:
# Sorts favorites by value using lambda function

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts
for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
    print(f"{favorite}: {counts[favorite]}")

# Notice that the get_value function has been removed. Instead, lambda language: counts[language] does in one line what our previous two-line function did.
# We can change the column we are examining, focusing on our favorite problem instead:
# Favorite problem instead of favorite language

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["problem"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print counts
for favorite in sorted(counts, key=lambda problem: counts[problem], reverse=True):
    print(f"{favorite}: {counts[favorite]}")

# Notice that problem replaced language.
# What if we wanted to allow users to provide input directly in the terminal? We can modify our code, leveraging our previous knowledge about user input:
# Favorite problem instead of favorite language

import csv

# Open CSV file
with open("favorites.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Counts
    counts = {}

    # Iterate over CSV file, counting favorites
    for row in reader:
        favorite = row["problem"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# Print count
favorite = input("Favorite: ")
if favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
# Notice how compact our code is compared to our experience in C.




"""
Relational Databases
Google, Twitter, and Meta all use relational databases to store their information at scale.
Relational databases store data in rows and columns in structures called tables.
SQL allows for four types of commands:
  Create
  Read
  Update
  Delete
These four operations are affectionately called CRUD.
We can create a SQL database at the terminal by typing sqlite3 favorites.db. Upon being prompted, we will agree that we want to create favorites.db by pressing y.
You will notice a different prompt as we are now inside a program called sqlite3.
We can put sqlite3 into csv mode by typing .mode csv. Then, we can import our data from our csv file by typing .import favorites.csv favorites. It seems that nothing has happened!
We can type .schema to see the structure of the database.
You can read items from a table using the syntax SELECT columns FROM table.
For example, you can type SELECT * FROM favorites; which will iterate every row in favorites.
You can get a subset of the data using the command SELECT language FROM favorites;.
"""
$ sqlite3 favorites.db
Are you sure you want to create favorites.db? [y/N] y
sqlite> .mode csv
sqlite> .import favorites.csv favorites
sqlite> .schema 
CREATE TABLE IF NOT EXISTS "favorites"("Timestamp" TEXT, "language" TEXT, "problem" TEXT);

$ sqlite3 favorites.db # re-abrir o CLI fora do sqlite> e abrir o arquivo .db que já criamos, pra ver de forma diferente as tabelas...

sqlite> SELECT * FROM favorites;
sqlite> SELECT language FROM favorites;
sqlite> SELECT Timestamp FROM favorites;
sqlite> SELECT COUNT(*) FROM favorites;
sqlite> SELECT COUNT(language) FROM favorites;
sqlite> SELECT DISTINCT(language) FROM favorites;
sqlite> SELECT COUNT(DISTINCT(language)) FROM favorites;
sqlite> 

"""
SQL supports many commands to access data, including:
  AVG
  COUNT
  DISTINCT
  LOWER
  MAX
  MIN
  UPPER
For example, you can type SELECT COUNT(language) FROM favorites;. Further, you can type SELECT DISTINCT(language) FROM favorites; to get a list of the individual languages within the database. You could even type SELECT COUNT(DISTINCT(language)) FROM favorites; to get a count of those.
"""

sqlite> SELECT COUNT(*) FROM favorites WHERE language = 'C';
sqlite> SELECT COUNT(*) FROM favorites;
sqlite> SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem = 'Mario';

sqlite> SELECT language, COUNT(*) FROM favorites GROUP BY language;
sqlite> SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*);
sqlite> SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) ASC;
sqlite> SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) DESC;
sqlite> SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*) DESC LIMIT 1;

sqlite> SELECT DISTINCT(language) FROM favorites;
sqlite> INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville');
sqlite> SELECT DISTINCT(language) FROM favorites;

sqlite> SELECT * FROM favorites WHERE language = 'C';
sqlite> UPDATE favorites SET language = 'C++' WHERE language = 'C';
sqlite> SELECT * FROM favorites WHERE language = 'C';
sqlite> SELECT * FROM favorites WHERE language = 'C++';

sqlite> UPDATE favorites SET language = 'C' WHERE language = 'C++';
sqlite> SELECT * FROM favorites WHERE language = 'C++';
sqlite> SELECT * FROM favorites WHERE language = 'C';

sqlite> DELETE FROM favorites WHERE problem = 'Tideman'; # Delete every entry from table with 'Tideman' as problem, including del of time and language...
sqlite> DELETE FROM favorites; # Delete everything from the table... XD lol...

"""
SQL offers additional commands we can utilize in our queries:

  WHERE       -- adding a Boolean expression to filter our data
  LIKE        -- filtering responses more loosely
  ORDER BY    -- ordering responses
  LIMIT       -- limiting the number of responses
  GROUP BY    -- grouping responses together

Notice that we use -- to write a comment in SQL.
For example, we can execute SELECT COUNT(*) FROM favorites WHERE language = 'C';. A count is presented.
Further, we could type SELECT COUNT(*) FROM favorites WHERE language = 'C' AND problem = 'Mario';. Notice how the AND is utilized to narrow our results.
Similarly, we could execute SELECT language, COUNT(*) FROM favorites GROUP BY language;. This would offer a temporary table that would show the language and count.
We could improve this by typing SELECT language, COUNT(*) FROM favorites GROUP BY language ORDER BY COUNT(*);. This will order the resulting table by the count.
We can also INSERT into a SQL database utilizing the form INSERT INTO table (column...) VALUES(value, ...);.
We can execute INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville');.
We can also utilize the UPDATE command to update your data.
For example, you can execute UPDATE favorites SET language = 'C++' WHERE language = 'C';. This will result in overwriting all previous statements where C was the favorite programming language.
Notice that these queries have immense power. Accordingly, in the real-world setting, you should consider who has permissions to execute certain commands.
DELETE allows you to delete parts of your data. For example, you could DELETE FROM favorites WHERE problem = 'Tideman';.
"""
    # Searches database popularity of a problem

    import csv
    from cs50 import SQL

    # Open database
    db = SQL("sqlite:///favorites.db")

    # Prompt user for favorite
    favorite = input("Favorite: ")

    # Search for title
    rows = db.execute("SELECT COUNT(*) FROM favorites WHERE problem LIKE ?", "%" + favorite + "%")

    # Get first (and only) row
    row = rows[0]

    # Print popularity
    print(row["COUNT(*)"])

    
    
"""
IMDb
IMDb offers a database of people, shows, writers, starts, genres, and ratings. Each of these tables is related to one another as follows:

    https://cs50.harvard.edu/x/2023/notes/7/cs50Week7Slide025.png
"""
# After downloading shows.db, you can execute sqlite3 shows.db in your terminal window.
Harvard-CS50/Week7/ $ ls
favorites.csv  favorites.db  favorites.py  shows.db
Harvard-CS50/Week7/ $ 
Harvard-CS50/Week7/ $ sqlite3 shows.db
sqlite> .schema

CREATE TABLE genres (
    show_id INTEGER NOT NULL,
    genre TEXT NOT NULL,
    FOREIGN KEY(show_id) REFERENCES shows(id)
);
CREATE TABLE people (
    id INTEGER,
    name TEXT NOT NULL,
    birth NUMERIC,
    PRIMARY KEY(id)
);
CREATE TABLE ratings (
    show_id INTEGER NOT NULL,
    rating REAL NOT NULL,
    votes INTEGER NOT NULL,
    FOREIGN KEY(show_id) REFERENCES shows(id)
);
CREATE TABLE shows (
    id INTEGER,
    title TEXT NOT NULL,
    year NUMERIC,
    episodes INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE stars (
    show_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY(show_id) REFERENCES shows(id),
    FOREIGN KEY(person_id) REFERENCES people(id)
);
CREATE TABLE writers (
    show_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY(show_id) REFERENCES shows(id),
    FOREIGN KEY(person_id) REFERENCES people(id)
);
# Upon executing .schema you will find not only each of the tables but the individual fields inside each of these fields.

# As you can see by the image above, shows has an id field. The genres table has a show_id field which has data that is common between it and the shows table.
# As you can see also in the image above, show_id exists in all of the tables. In the shows table, it is simply called id. This common field between all the fields is called a key. Primary keys are used to identify a unique record in a table. Foreign keys are used to build relationships between tables by pointing to the primary key in another table.
# By storing data in a relational database, as above, data can be more efficiently stored.
# In sqlite, we have five datatypes, including:
#      BLOB       -- binary large objects that are groups of ones and zeros
#      INTEGER    -- an integer
#      NUMERIC    -- for numbers that are formatted specially like dates
#      REAL       -- like a float
#      TEXT       -- for strings and the like
# Additionally, columns can be set to add special constraints:
#      NOT NULL     -- may or may not let NULL (blank values) in a column, like 'Timestamp' lacking data in INSERT TO above 'SQL', 'Fiftyville'.
#      UNIQUE       -- unique number that can not have two versions of, like CPF, email, social security number...
# To illustrate the relationship between these tables further, we could execute the following command: SELECT * FROM people LIMIT 10;. Examining the output, we could execute SELECT * FROM shows LIMIT 10;. Further, we could execute SELECT * FROM stars LIMIT 10;. show_id is a foreign key in this final query because show_id corresponds to the unique id field in shows. person_id corresponds to the unique id field in the people column.

sqlite> SELECT * FROM people;
sqlite> SELECT * FROM people LIMIT 10; 
sqlite> SELECT * FROM shows LIMIT 10; 
sqlite> SELECT * FROM stars LIMIT 10;

sqlite> SELECT * FROM genres LIMIT 10;
sqlite> SELECT * FROM genres WHERE genre = 'Comedy' LIMIT 10;
sqlite> SELECT * FROM shows WHERE id = 62614;
sqlite> SELECT * FROM shows WHERE id = 63881;
sqlite> SELECT * FROM shows WHERE id = 65270;

sqlite> SELECT show_id FROM genres WHERE genre = 'Comedy';
sqlite> SELECT COUNT(show_id) FROM genres WHERE genre = 'Comedy';
sqlite> SELECT title FROM shows WHERE id IN (SELECT show_id FROM genres WHERE genre = 'Comedy');
sqlite> SELECT title FROM shows WHERE id IN (SELECT show_id FROM genres WHERE genre = 'Comedy') LIMIT 10;
sqlite> SELECT title FROM shows WHERE id IN (SELECT show_id FROM genres WHERE genre = 'Comedy') ORDER BY title LIMIT 10;

# We can further play with this data to understand these relationships. Execute SELECT * FROM genres;. There are a lot of genres!
# We can further limit this data down by executing SELECT * FROM genres WHERE genre = 'Comedy' LIMIT 10;. From this query, you can see that there are 10 shows presented.

sqlite> SELECT * FROM people WHERE name = 'Steve Carell';
SELECT * FROstars WHERE person_id = 136797; 
#+----------+-----------+
#| show_id  | person_id |
#+----------+-----------+
#| 115148   | 136797    |
#| 118420   | 136797    |
#| 306410   | 136797    |
#| 381741   | 136797    |

sqlite> SELECT title FROM shows WHERE id = 115148;
sqlite> SELECT title FROM shows WHERE id = 118420;
sqlite> SELECT * FROM people WHERE name = 'Steve Carell';
sqlite> SELECT id FROM people WHERE name = 'Steve Carell';
sqlite> SELECT * FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Steve Carell');
sqlite> SELECT show_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Steve Carell');
sqlite> SELECT title FROM shows WHERE id IN (SELECT show_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Steve Carell'));
sqlite> SELECT title FROM shows WHERE id IN (SELECT show_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Steve Carell')) ORDER BY title;

# You can discover what shows these are by executing SELECT * FROM shows WHERE id = 626124;
# We can further our query to be more efficient by executing

    SELECT title
    FROM shows
    WHERE id IN (
        SELECT show_id
        FROM genres
        WHERE genre = 'Comedy'
    )
    LIMIT 10;

# Notice that this query nests together two queries. An inner query is used by an outer query.
# We can refine further by executing

    SELECT title
    FROM shows
    WHERE id IN (
        SELECT show_id
        FROM genres
        WHERE genre = 'Comedy'
    )
    ORDER BY title LIMIT 10;

# What if you wanted to find all shows in which Steve Carell stars? You could execute SELECT * FROM people WHERE name = 'Steve Carell'; You would find his individual id. You could utilize this id to locate many shows in which he appears. However, this would be tedious to attempt this one by one. How could we next our queries to make this more streamlined? Consider the following:

    SELECT title FROM shows WHERE id IN
      (SELECT show_id FROM stars WHERE person_id =
        (SELECT * FROM people WHERE name = 'Steve Carell'));

# Notice that this lengthy query will result in a final result that is useful in discovering the answer to our question.
