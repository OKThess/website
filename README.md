# OK!Thess

Django application, powers [okthess.gr](http://okthess.gr/).


## Setup

Install requirements:
```
pip3 install -r requirements.txt
```

Then, migrate your database:
```
python3 manage.py migrate
```

Finally, run the Django server:
```
python3 manage.py runserver
```

The Django project is `avocado`. There is one Django app, `main`, which includes
all business logic.
