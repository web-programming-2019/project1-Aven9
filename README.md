# Project 1

The project build a simple application with Flask, Postgresql and Goodread API. Templates directory saves all html files, within `template1.html` and `template2.html` are used as template for `login.html`, `signin.html` and `search.html`, `detail.html` pages respectively. All routes relative is in application.py

## Sign in, log in and log out

1. The first page is initialized `index.html`, **sign in** and **login** hyper link is added for testing.
2. Sign in route creates user, store it in database with **users(username, password)** table.
3. Login route search **users** for a match with input username and password. 
4. Log out route just returns a **login page**. 
5. Once user login, the **username** will be passed as a parameter from a route to another for validating itself.

## Import books' information 

`import.py` creates table **books**(isbn, title, pubyear, author), and stores all rows from `book.csv` into table **books**.

## Search for books

Search route searches table **books** for results according to isbn, title or author and display them in current page. To achieve ambiguous search, `like` keyword is used.

## Display detail

1. Detail page displays all columns information in **books** for a book. 
2. It also call Goodread API for displaying rating information about a book.
3. Review input is provided if user has NOT committed a review about the book. The function implemented by Jinja2, using variable for storing all users in comments. If user is  in users, input should not be displayed.
4.  Review is stored in a table named **review(id, isbn, username, rank, content)**, displayed by searching **review**.

## API

API route creates json result for a book according to isbn information.

## UI

To make user interface is not that ugly, bootstrap is used in templates.