## Youwu.life

A web based social network made for those who desire a place to showcase,
keep track of the anime they love and to explore the anime that friends
love in one place. It gives the user the ability to create a custom user 
profile and add anime from a large database that should contain the anime 
of their choosing as well as a friends profile to keep up with what they 
are watching, without the need to piece information together about anime
from multipal external websites.



## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org).

Heroku CLI installed (https://devcenter.heroku.com/articles/heroku-cli)
(need an account)

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
