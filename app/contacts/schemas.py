## imports
from app import ma

from . import Contact


class ContactSchema(ma.Schema):
    fields = ('id', 'account', 'name', 'phone', 'email', 'joined_on')


contact_schema = ContactSchema()    
contacts_schema = ContactSchema(many=True)    