# Capstone 1

Webscrapper for the NAMI Urban Los Angeles Resource Page

## Overview: 
A web application that allows users to retrieve the individual resource weblinks from the NAMI Urban Los Angeles Resource webpage using resource categories. 

## Tech Stack:
- Backend: 
Python, Flask
- Frontend: 
Bootstrap, jQuery, Jinga
- Libraries:
BeauitfulSoup
- API/Website Used for Scrapping: 
https://www.namiurbanla.org/resources

## App Features Include:
- User can choose a resource category from the dropdown menu, featured on the homepage
- For chosen category, a list of weblinks will be rendered onto the following page

## Setup/Installation:
- Create/Activate Virtual environment:
```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
```

- Install dependencies:
```bash
    $ pip3 install -r requirements.txt
```

- Pass in Environment Variables:
```bash
    $ export FLASK_ENV=development
    $ export FLASK_APP=app.py
```

- Run the app:
``` bash    
    $ flask run
```

Open localhost:5000 on Browser




