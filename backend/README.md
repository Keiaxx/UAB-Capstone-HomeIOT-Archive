# HomeIOT REST API

This REST API is designed with Python, Flask, and Flask-RESTplus to aid in API documentation via Swagger.

## Python3 Dependencies
A quick list of dependencies needed are below. You can use venv/pipenv or just install them globally
as you wish
```
Flask
Flask-SQLAlchemy
flask-restplus
```

## Running the app

Before running `app.py`, we must first generate some dummy data to work with. Run the data generator in the
`data_generator` subfolder and run `generate.py`

Currently, I have configured it to create a dummy SQLite db which will aid in local testing and
development, and later on we can migrate to the UAB PostgreSQL database easily.

Once `generate.py` has been run, we can now run

```bash
python3 app.py
```

which will run the local app at http://localhost:5000/

When you visit http://localhost:5000/ , you will see the Swagger API documentation, which is
dynamically generated based on the annotations you provide in the view spec under the `views` subfolder

