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
CREATE TABLE IF NOT EXISTS "favorites"(
"Timestamp" TEXT, "language" TEXT, "problem" TEXT);
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
