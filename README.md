# ML web app with Flask example: movie recommendation engine

## Introduction

This repository contains the minimum requirements to get a public web application up and working using a model from one of our prior projects. I have completed much of the nit-picky configuration already, but it's up to you to build the heart of the application and deploy it to Render.

The project consists of four components:

1. **[Recommender function](https://github.com/4GeeksAcademy/gperdrizet-k-nearest-neighbors/blob/main/src/solution.ipynb)**: This function is the heart of the app. You will write it in Python. It takes a movie title from the user and returns movie recommendations.
2. **[Flask](https://flask.palletsprojects.com/en/stable/)**: Flask is a simple web application framework, it will act as the go-between to bridge the html world of the user's web-browser and our internal python functions.
3. **[Gunicorn](https://gunicorn.org/)**: Gunicorn is the webserver that will serve the page to users and send data to our application via Flask.
4. **[Render](https://render.com/)**: Render is the cloud hosting service we will use to actually run our application. This allows us to have a public URL where the application can be accessed by users.

## Render deployment

Once you have your application running in a codespace with no errors, it is time to deploy to Render. Go to [render.com](https://render.com/) and click 'Get started for free'. The site will ask for an email address and password and then send you a conformation link. After clicking the link, you are asked to fill out some basic profile details and finally taken to the 'service type' page on the Render Dashboard page. From there we create a new service for our application:

1. Choose 'New web service' from the service type dashboard tab
2. On the Configure tab, select 'Public Git Repository' and paste the link to your project repository
3. Click 'Connect'

This will take you to the new webservice's dashboard. Then, from the settings tab set the following values:

1. **Name**: whatever you want
2. **Project**: don't need to add to a project for a minimal deployment
3. **Language**: Python 3
4. **Branch**: main
5. **Region**: Ohio (US east) - or whatever is closest to you
6. **Root directory**: don't set
7. **Build Command**: ./setup.sh
8. **Start Command**: gunicorn src.app:app

After that, set the instance type to free, and you can leave everything else alone. Click 'Deploy Web Service'! You should see the requirements.txt being installed in the log terminal and then gunicorn starting. If there were no problems, you can now access your web app at the URL provided at the top of the page, under the project name and GitHub repository link.
