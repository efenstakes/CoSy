## imports
from flask_restful import Resource, reqparse


## add
class ContactAdd(Resource):

    def post(self):
        return 'add'


## update
class ContactUpdate(Resource):

    def put(self):
        return 'update'


## delete
class ContactDelete(Resource):

    def delete(self):
        return 'delete'


## get details
class ContactDetails(Resource):

    def get(self, id):
        return 'details'


## get all
class ContactsAll(Resource):

    def get(self):
        return 'all contacts'

