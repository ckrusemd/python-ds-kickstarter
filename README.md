Python Data Science Kickstarter 
==============================

<p><small>Based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

Builds on top of the excellent Cookiecutter DS template with services for FastAPI, Dash, MongoDB and pytest-html (creating a nice HTML of collected tests and displaying them through nginx).

I base other projects on this template and invite you to do the same - please raise issues and suggestions.

Docker services:
- FastAPI
- Plotly Dash
- MongoDB 
- Pytest-html (with nginx)

How to run:
* docker-compose up -d

Default services:
* FastAPI: 127.0.0.1:8080/docs
* Dash: 127.0.0.1:8050
* MongoDB: 127.0.0.1:27017
* Pytest-html: 127.0.0.1:80