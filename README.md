# Handling ML Predictions in a Flask App

_created by Austin Poor_

This repo demonstrates a technique for handling long-running processes (like ML model predictions)
inside a Flask app, by passing them off to Celery.

While this is just a simple example, the same workflow could help in cases where you're performing
slow, complicated tasks like making ML predictions, building recommendations, or updating a database.

## Demo

![](images/demo.gif)

The app is composed of Redis (the broker and backend for Celery), a Celery worker, and then the Flask app.

The Flask app is composed of a simple HTML landing page and two API endpoints.

The HTML page has 4 range sliders, allowing you to choose values for the width and height of the 
iris's sepal and petal, for prediction.

When you click the `Submit` button, a javascript function sends the parameters in a POST request to
`/api/predict`, which schedules the prediction with the Celery worker, and returns the `taskid`
that will store the result.

Then, after making the request, the browser polls the second API endpoint (`/api/get-result/<taskid>`)
until the status changes from pending to `SUCCESS` (or to an error). It then updates the status and
the prediction table.


## Instructions to Run

__Requirements__
* `Python 3.6+`
* `scikit-learn`
* `Docker` & `docker-compose`

1. Download the repo
2. Train the ml model with the [train.py](./train.py) script
3. Build and run the containers with `docker-compose up --build`
4. Then go to [localhost:5000](http://localhost:5000)

