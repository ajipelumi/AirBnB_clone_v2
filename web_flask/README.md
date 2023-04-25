**Flask** is a lightweight Python web framework that makes it easy to build web applications.

Here are basic steps to build a simple web framework with Flask:

1. Install Flask: The first step is to install Flask. We can use pip to install Flask by running the following command in our terminal or command prompt:
```bash
$ pip install flask
```

2. Create the application: The next step is to create a new Flask application. This can be done by creating a new Python file and importing the Flask module:
```python
from flask import Flask

app = Flask(__name__)
```
The `__name__` argument tells Flask to use the current module as the application name.

3. Define the routes: Flask uses routes to map URLs to specific functions in your code. We can define a route by using the `@app.route` decorator:
```python
@app.route('/')
def index():
    return 'Hello, world!'
```
This route maps the root URL (`/`) to a function called index(), which returns the string '**Hello, world!**'.

4. Run the application: Finally, we can run the Flask application by running the following command in our terminal:
```bash
$ export FLASK_APP=app.py
$ flask run
```
This will start the development server and make our application available at *http://localhost:5000/*.

From here, we can add more routes, views, and functionality to build a more complex web framework.
