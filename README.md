# Fitness Management System

## Project Overview
The Fitness Management System is a graphical user interface (GUI) application built using Python’s Tkinter library and connected to a MySQL database. This system allows for the management of gym members, including adding, viewing, and organizing member data.

## Features

Add New Members: Capture essential details like name, age, membership type, email, phone, and join date.

View Members: Display all members’ details in a table format with sortable columns.

Database Integration: Stores data in a MySQL database, ensuring data persistence and efficient retrieval.

User-Friendly Interface: Uses Tkinter for a simple and intuitive interface.


## Requirements
Python: Version 3.x

Tkinter: Installed with Python

MySQL Database: A MySQL server installed locally or remotely

mysql-connector-python: Install via pip install mysql-connector-python

## Installation
1. Set Up Python and Required Packages

Install Python 3 if not already installed.
Open your terminal (or Command Prompt) and run:

```bash
pip install mysql-connector-python
```
2. Set Up the Database
Open MySQL and create the project database with these commands:
```bash
CREATE DATABASE fitness_db;
USE fitness_db;
```
Create the members table in this database:
```bash
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    membership_type VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    join_date DATE NOT NULL
);
```
Run the Python Program
Download or place the Python project files in a folder.

Open a terminal in that folder, and start the program by running
```bash
python fitness_management_system.py
```

# Usage Steps
## Adding a New Member
Enter the details for each field (name, age, etc.) and click Add Member.
Ensure the age is a number, and the join date follows the format DD-MM-YYYY.

## Viewing All Members
Click View Members to display the list of members in the table at the bottom.

Scroll through to see all member details.

## Clearing Input Fields
To clear all fields, manually delete the text or add a reset button if needed.

Ensure your MySQL server is running to connect to the database.

Make sure the database and table names match exactly as shown in the setup steps.

##  Queries to fetch specific data
```bash
SELECT * FROM members;
SELECT name FROM members WHERE membership_type = 'Yearly';
SELECT name FROM members WHERE age = 30;
SELECT name FROM members WHERE age = 34;
SELECT COUNT(*) AS total_members FROM members;
SELECT AVG(age) AS average_age FROM members;
SELECT MAX(age) AS max_age FROM members;
SELECT MIN(age) AS min_age FROM members;
SELECT membership_type, COUNT(*) AS count FROM members GROUP BY membership_type;

-- Delete all inserted rows safely
DELETE FROM members WHERE member_id > 0;  -- Deletes all records

```

