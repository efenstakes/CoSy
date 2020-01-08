## imports
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS


## create flask object
app = Flask(__name__, instance_relative_config=True)
## set app configuration
app.config.from_object('config.Config')
## allow cross origin requests
CORS(app)

## create an sqlalchemy object
db = SQLAlchemy(app)
## create a marshmallow object
ma = Marshmallow(app)


## import module blueprints
from .contacts import contacts_bp 
from .accounts import accounts_bp


## add the module blueprints to the app instance
app.register_blueprint(contacts_bp, url_prefix='/api/contact')
app.register_blueprint(accounts_bp, url_prefix='/api/account')



''' before the server serves any request '''
@app.before_first_request
def before_any_request():
    with app.app_context():
        db.create_all()
    print('starting server...')



## import jwt authentication middleware
from .auth import *


### create more routes

# index
@app.route('/')
def index():
    return { 'page': 'index', 'live': True }

# about
@app.route('/about')
def about():
    return { 'page': 'about', 'live': True }