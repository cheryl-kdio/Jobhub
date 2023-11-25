# JobHub: Simplifying Job Search in the Tech Sector

Welcome to JobHub, an application designed to streamline the job search process in the technology sector. To ensure the proper functioning of the application, please follow the instructions below.

## Database Configuration

The SQL tables presented in our Relational Database Diagram (RDB) have been stored in a database named "projet2A." To initialize this database, execute the `Utils/reset_database.py` module. Also, make sure you have correctly configured your credentials in the `.env` file to initialize these tables in your DBeaver sessions at ENSAI.

> **Attention:** The host of our database is defined as `sgbd-eleves.domensai.ecole`. If you are not on an ENSAI virtual machine (view7.ensai.fr), the application will not function correctly. If you intend to run our application locally, make sure to modify the host and related database information accordingly.

## Project Description

This project aims to create an application that simplifies job searching in the technology sector using the free REST API from [Adzuna](https://developer.adzuna.com/), which provides information on job listings in various sectors worldwide. The application allows users to search for jobs, filter results, track their application progress, and receive alerts for new listings matching their skills.

## Project Objectives

The primary objectives of this project are as follows:

- Integrate Adzuna API data into a user-friendly application.
- Allow users to search for job listings by keywords, location, and categories.
- Provide features for tracking applications, including managing CVs and cover letters.
- Send alerts to users for new job listings matching their criteria.
- Implement a user profile system for job seekers.

## Application Features

Our application caters to individuals seeking internships or jobs in the technology sector. It offers the following features:

- [ ] Create an account
- [ ] Log in to an account
- [ ] Search for job listings
- [ ] Save job listings
- [ ] Apply to job listings
- [ ] Track job applications
- [ ] Receive alerts for new listings matching criteria

All these features are accessible through Python views in the terminal. To access them, please run only the `main.py` file. Also, ensure you have installed all the required packages using the `pip install -r requirements.txt` command.

In the future, we plan to develop a graphical user interface to make the application even more user-friendly.

## Technologies Used

The technologies used in this project include:

- Python
- PostgreSQL via DBeaver
- Adzuna API

## Project Information

This project is part of the second-year curriculum of the Complementary Computer Science course at ENSAI. It allowed us to apply our skills in object-oriented programming, project management, and database management.

**Group Members:**
- Benjamin Guéraud
- Beedi Goua
- Antoine Jarry
- Cheryl Kouadio
- Clara Serano

**Supervisor:** Mansour GUEYE

Stay tuned for upcoming features and improvements in JobHub!
![](https://giphy.com/gifs/spongebob-spongebob-squarepants-episode-9-3oKHWtGyQrx7CwV8li)

