## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

```sh
$ git clone https://github.com/heroku/python-getting-started.git
$ cd python-getting-started

$ python3 -m venv getting-started
$ pip install -r requirements.txt

$ createdb python_getting_started

$ python manage.py migrate
$ python manage.py collectstatic

If you’re on Microsoft Windows system, run this:
heroku local web -f Procfile.windows

If you’re on a Unix system, just use the default Procfile by running:
heroku local web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

Using: Python: 3.7.5