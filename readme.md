# Minimal Heroku python setup project
This project is the minimal python setup to run in cloud environment on Heroku.
With this you will be able to deploy your application to the cloud automatically just by updating your GitHub repository.
Few examples and basic authentication included.

# How it works
- run_srv.py starts internal Flask server and handles all requests, including basic authentication
- requirements.txt store package names required for your project
- Procfile is used by Heroku to start it's web server (gunicorn)
- heroku.yml is a config file for Heroku
- .html files are just for demonstration

# Instructions
- Download or clone this repository. You can add these files to your existing project.
- Install requirements from requirements.txt:
~~~
pip install -r requirements.txt
~~~
- Put all your packages back to requirements.txt (Heroku needs to know what to install):
~~~
pip freeze > requirements.txt
~~~
- Register on Heroku.com and link your GitHub repository and branch on the Deploy tab of your application
- Optional: set up BASIC_AUTH_USERNAME and BASIC_AUTH_PASSWORD variables on Heroku Settings tab to enable simple authentication (just 1 user)