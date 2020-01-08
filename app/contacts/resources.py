## imports
from flask_restful import Resource, reqparse

from app import db
from . import Contact, contact_schema, contacts_schema



## add
class ContactAdd(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('account', type=str, required=True, help='Contact account shoudl be provided')
    parser.add_argument('name', type=str, required=True, help='Contact name shoudl be provided')
    parser.add_argument('email', type=str, required=False)
    parser.add_argument('phone', type=str, required=True, help='Contact phone shoudl be provided')

    def post(self):
        responze = { 'saved': False, 'contact': None }

        ## get user input
        data = self.parser.parse_args()
        name = data['name']
        email = data['email']
        phone = data['phone']
        account = data['account']

        try:
            contact = Contact( 
                        name=name, email=email, 
                        phone=phone, account=account 
                    )
            db.session.add(contact)
            db.session.commit()
        except:
            return responze, 500

        responze['saved'] = True 
        responze['contact'] = contact_schema.dump(contact)
        return responze


## update
class ContactUpdate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=False)
    parser.add_argument('phone', type=str, required=True, help='Contact phone shoudl be provided')

    def put(self, name):
        responze = { 'saved': False, 'contact': None }

        ## get user input
        data = self.parser.parse_args()
        email = data['email']
        phone = data['phone']

        try:
            contact = Contact.query.filter_by( name=name ).get()
            contact.phone = phone
            contact.email = email
            db.session.commit()
        except:
            return responze, 500

        responze['saved'] = True 
        responze['contact'] = contact_schema.dump(contact)
        return responze


## delete
class ContactDelete(Resource):

    def delete(self, id):
        responze = { 'deleted': False }

        try:
            contact = Contact.query.get(id)
            db.session.delete(contact)
            db.session.commit()
        except:
            return responze, 400

        responze['deleted'] = True
        return responze


## get details
class ContactDetails(Resource):

    def get(self, id):
        responze = { 'contact': None }

        try:
            contact = Contact.query.get(id)
        except:
            return responze, 404

        responze['contact'] = contact_schema.dump(contact)
        return responze


## get all
class ContactsAll(Resource):

    def get(self, account):
        responze = { 'contacts': [] }

        try:
            contacts = Contact.query.filter_by(account=account).all()
        except:
            return responze, 500

        responze['contacts'] = contacts_schema.dump(contacts)
        return responze

