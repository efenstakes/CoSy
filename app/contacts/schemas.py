## imports
from app import ma

from . import Contact


class ContactSchema(ma.Schema):
    fields = ('id', 'name', 'phone', 'email', 'joined_on')