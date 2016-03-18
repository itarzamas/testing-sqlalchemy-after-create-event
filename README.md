# Testing SQLAlchemy 'after_create' event in a Flask application

The prototype of a Flask app, that uses plain SQLAlchemy models with the Flask-SQLAlchemy session.
It was created to test <code>'after_create'</code> event from SQLAlchemy event API. The app uses it to insert
initial values just once after database creation.<br>

The app inserts into <code>priority</code> table values: <code>high</code>, <code>medium</code>, <code>low</code>.
It ilustrates the graphics below.

<img src="https://dzone.com/storage/temp/1284139-vertabelo-model.png"/>

I presented more detailed description in the DZONE article: https://dzone.com/articles/how-to-initialize-database-with-default-values-in 
