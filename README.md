# ML web app with Streamlit: movie recommendation engine

[![Pytest](https://github.com/4GeeksAcademy/gperdrizet-recommender-system-streamlit/actions/workflows/pytest.yml/badge.svg)](https://github.com/4GeeksAcademy/gperdrizet-recommender-system-streamlit/actions/workflows/pytest.yml)
[![Codespaces Prebuilds](https://github.com/4GeeksAcademy/gperdrizet-recommender-system-streamlit/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg)](https://github.com/4GeeksAcademy/gperdrizet-recommender-system-streamlit/actions/workflows/codespaces/create_codespaces_prebuilds)

Service is live on [Render](https://movie-recommender-streamlit.onrender.com).

**Note**: Render 'scales to zero', so it may take a few minutes for the service to start back up if no one has used it in a while.

## Introduction

This repository contains a minimal public web application deployment of the movie recommendation model we built earlier in the course.

The project consists of three components:

1. **[Recommender function](https://github.com/4GeeksAcademy/gperdrizet-recommender-systems/blob/main/notebooks/solution.ipynb)**: This Python function is the heart of the app. It takes a movie title and uses a k-nearest neighbors and a movie database to return recommendations of other similar movies.
2. **[Streamlit](https://streamlit.io/)**: Streamlit is a web application framework, it will act as the go-between to bridge the html world of the user's web-browser and our internal python functions.
4. **[Render](https://render.com/)**: Render is the cloud hosting service we will use to actually run our application. This allows the app to have a public URL where it can be accessed by users.

## Local testing

To test your app locally inside your codespace run the following command in the terminal:

```bash
streamlit run src/movie_recommender.py
```

This will allow you to test the app out, without having to actually deploy it to Render and will save you a lot of time. Once everything is working, it's time to deploy.

## Render deployment

Go to [render.com](https://render.com/) and click 'Get started for free'. The site will ask for an email address and password and then send you a conformation link. After clicking the link, you are asked to fill out some basic profile details and are finally taken to the [Render Dashboard](https://dashboard.render.com/). From there, we can create a new service for our application:

1. Click '+ New' button at the top right and select 'Web Service' from the dropdown menu
2. Select 'Public Git Repository' and paste the link to your project repository
3. Click 'Connect'

This will take you to the new web service dashboard. Then, from the settings tab set the following values:

1. **Name**: whatever you want
2. **Project**: don't need to add to a project - this is generally for more complex deployments that comprise multiple services
3. **Language**: Python 3
4. **Branch**: main
5. **Region**: Ohio (US east) - or whatever is closest to you
6. **Root directory**: don't set
7. **Build Command**: pip install requirements.txt
8. **Start Command**: streamlit run ./src/movie_recommender.py

After that, set the instance type to free, and you can leave everything else alone. Click 'Deploy Web Service'! You should see the setup.sh script being run in the log terminal. If there were no problems, you can now access your web app at the URL provided at the top of the page, under the project name and GitHub repository link.
