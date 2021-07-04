# hillel_hw11

To run in a production mode run:
./manage.py runserver --settings=hillel_hw11.settings.production

Database population:
1) Management command load_data 
2) bookstore/fixtures/db.json

To run celery worker run:
celery -A hillel_hw11 worker -l INFO