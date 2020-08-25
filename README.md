# Gamers-Paradise : A WebApp

A web application for gamers

Project Idea:

Gamers often don’t know which games to buy, since there is a large variety to pick from.
This variety arises due to different consoles, gaming genres, game producer, popularity, etc. We wanted to make an application which gives a one-stop solution to the above problems.

Our web application will give a gamer insight into the best-selling games of the last 40 years, based on different criteria such as sales, genre, publisher, console availability, game versions, etc. This will help him/her to buy a game after a quick one-stop analysis.
Technology Stack Used:


Database - Firebase
Server-side scripting - Flask
Front-end - HTML, CSS, JavaScript
Dataset: “Video Game Sales” https://www.kaggle.com/gregorut/videogamesales Shape of the Data Set: 16,600 rows x 11 columns

Contents-

The .html files are the diff templates which are 'rendered' by flask upon different button/function calls ( these are part of 'templates' folder.

The .png files are part of the 'static' folder.

Drawer.py - codes the logic for the charts and graphs in the 'static' part of the application.
loader.py - codes for loading the data into firebase
simple.py - codes the core logic for the entire application

Yr_filter_1984-1993.png, name_sort.png - two of the screenshots of the web app ( for year filter and name sort)
