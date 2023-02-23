# Django-Generate-Fake-Data

**virtual enviroment**
- Creating -> python3 -m venv env
- starting -> source env/bin/activate
- closeing -> deactivate

# 1- Faker?
- is a python package that generates fake data for database.
- installing -> pip install Faker

# 2- When do we use Faker?
- at a start of the project
- scale data in the database for testing its performance
- test application

# 3- In this project:
- 1- setup faker with django
    - create a directory -> management/commands/createdata.py in the app you want to use fake data for
    - add these in createdata.py:
        - - from django.core.management.base import BaseCommand
        - - from faker import Faker

        - - class Command(BaseCommand):
            - - help = "Command Information"

            - - def handle(self, *args, **kwargs):
                - - fake = Faker()
                    **use faker providers here.**
    - 
- 2- creating data (providers)
    - providers -> are list of information you might want to use.
- 3- faker localization
    - choose a language for data
        - fake = Faker(["fa_IR"])
- 4- custom provider
    - import faker.providers 
    - create lists of fake data
    - create class and make functions for choose fake data 
- 5- custom management command

**For this project we use fix set of data (use fixture library)**
# Fixture?
- a collection of data that django knows how to import into a database.

