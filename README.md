# hillel_hw11

To run in a production mode run:
./manage.py runserver --settings=hillel_hw11.settings.production

Database population for bookstore app:
1) Use management command: ./manage.py load_data
2) Fixture: ./manage.py loaddata db.json

Database population for rediscache app:
1) Use management command: ./manage.py load_mydata
2) Fixture: ./manage.py loaddata mydb.json

To run celery worker run:
celery -A hillel_hw11 worker -l INFO

To run celery worker + celery beat run:
celery -A hillel_hw11 worker -B -l INFO