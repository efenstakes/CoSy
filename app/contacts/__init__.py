## imports
from flask import Blueprint
from flask_restful import Api

## models
from .models import Contact

## schemas
from .schemas import (

)

## resources
from .resources import (
    ContactAdd, ContactUpdate, ContactDelete, ContactDetails,
    ContactsAll
)

## create contact blueprint
contacts_bp = Blueprint('contacts_bp', __name__)
contacts_api = Api(contacts_bp)


## add api routes
contacts_api.add_resource(ContactAdd, '/')
contacts_api.add_resource(ContactUpdate, '/<id>')
contacts_api.add_resource(ContactDelete, '/<id>')
contacts_api.add_resource(ContactDetails, '/<id>')
contacts_api.add_resource(ContactsAll, '/')