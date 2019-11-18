## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org).
and Heroku CLI installed (https://devcenter.heroku.com/articles/heroku-cli)

```sh
$ git clone git@github.com:Four-Jacks/anime-social-network.git
$ cd anime-social-network

$ python3 -m venv anime-social
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py collectstatic

If you’re on Microsoft Windows system, run this:
heroku local web -f Procfile.windows

If you’re on a Unix system, just use the default Procfile by running:
heroku local web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

Using: Python: 3.7.5
