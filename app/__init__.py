## imports
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy 


## create flask object
app = Flask(__name__, instance_relative_config=True)
## set app configuration
app.config.from_object('config.Config')

## create an sqlalchemy object
db = SQLAlchemy(app)
## create a marshmallow object
ma = Marshmallow(app)



## import module blueprints
from .contacts import contacts_bp 


## add the module blueprints to the app instance
app.register_blueprint(contacts_bp, url_prefix='/api/contact')

## create more routes

# index
@app.route('/')
def index():
    return { 'page': 'index', 'live': True }

# about
@app.route('/about')
def about():
    return { 'page': 'about', 'live': True }