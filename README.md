## FTL_CodingChallenge
Coding challenge for Full Throttle Labs


## Installation

Clone the project in your evironment

Navigate to the directory

Create python virtual environment

Install project enviroment requirements

```bash
pip install -r requirements.txt
```

## Setup Database

Navigate to full_throttle_labs directory where manage.py file resides

```bash
python manage.py migrate
```

## Usage

To populate DB with dummy data using custom management command 'populate_db'

```bash
python manage.py populate_db n  # n is an integer value which tells the number of records to populate
```

Example:

```bash
python manage.py populate_db 5  # Creates 5 member records and 5 activity_period records per member
```

To create superuser

```bash
python manage.py createsuperuser
```
Follow along with the inputs asked


To run development server

```bash
python manage.py runserver
```
By default the server runs on port 8000

On the browser go to localhost:8000

For admin site go to localhost:8000/admin
Login using the superuser created in one of the previous steps

To view the api which serves data go to localhost:8000/member/api/member_activity/


## Hosted Web App
This webapp is also hosted on a public accessible location @ http://architjha.pythonanywhere.com/

To view the api which serves data go to http://architjha.pythonanywhere.com/member/api/member_activity/

