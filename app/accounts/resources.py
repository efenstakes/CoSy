import datetime
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash
from flask_jwt_extended import (
    jwt_required, current_user, create_access_token
)

from . import Account, account_schema, accounts_schema
from app import db


## create new
class AccountCreate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name should be provided')
    parser.add_argument('email', type=str, required=True, help='Email should be provided')
    parser.add_argument('password', type=str, required=True, help='Password should be provided')
    parser.add_argument('password_confirmation', type=str, required=True, help='Password Confirmation should be provided')

    def post(self):
        responze = { 'saved': False, 'user': None }

        data = self.parser.parse_args()

        try:
            account = Account(
                name=data['name'], email=data['email'],
                password=generate_password_hash(data['password']),
                public_id = 'xxx'
            )
            db.session.add(account)
            sb.session.commit()
        except:
            return responze, 500

        responze['saved'] = True 
        responze['user'] = account_schema.dump(account)
        return responze  


## update
class AccountUpdate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name should be provided')
    parser.add_argument('email', type=str, required=True, help='Email should be provided')

    @jwt_required
    def put(self, id):
        responze = { 'updated': False, 'user': None }

        data = self.parser.parse_args()
        try:
            account = Account.query.filter_by(id=current_user.id).first()
            account.name = data['name']
            account.email = data['email']
            
            sb.session.commit()
        except:
            return responze, 404

        responze['updated'] = True
        responze['user'] = account_schema.dump(account)
        return responze  


## update password
class AccountUpdatePassword(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str, required=True, help='Password should be provided')
    parser.add_argument('password_confirmation', type=str, required=True, help='Password Confirmation should be provided')

    @jwt_required
    def put(self, id):
        responze = { 'updated': False, 'user': None }

        data = self.parser.parse_args()

        try:
            account = Account.query.filter_by(id=current_user.id).first()
            account.password = generate_password_hash(data['password'])
            
            sb.session.commit()
        except:
            return responze, 404

        responze['updated'] = True
        responze['user'] = account_schema.dump(account)
        return responze  


## delete
class AccountDelete(Resource):

    @jwt_required
    def delete(self, id):
        responze = { 'deleted': False }

        try:
            Account.query.filter_by(id=current_user.id).first()
            
            db.session.delete(account)
            sb.session.commit()
        except:
            return responze, 404

        responze['deleted'] = True
        return responze


## get details
class AccountDetails(Resource):

    def get(self, id):
        responze = { 'user': None }

        try:
            account = Account.query.get(id)
        except:
            return responze, 404

        responze['user'] = account_schema.dump(account)
        return responze


## check if a name or email is used
class AccountNameOrEmailUsed(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=False, )
    parser.add_argument('email', type=str, required=False, )
   
    def get(self):
        responze = { 'used': None }

        ## get user input
        data = self.parser.parse_args()
        name = data['name']
        email = data['email']

        ## if both are null, abort
        if not name and not email:
            return responze, 400

        try:
            if name and email:
                account = Account.query.filter_by(name=name, email=email).first()
                
            if name and not email:
                account = Account.query.filter_by(name=name).first()
                
            if email and not name:
                account = Account.query.filter_by(email=email).first()
        except:
            responze['used'] = False 
            # return responze, 404

        responze['used'] = True
        return responze


## log a user in
class AccountLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='Email should be provided')
    parser.add_argument('password', type=str, required=True, help='Password should be provided')

    def post(self):
        responze = { 'user': None, 'token': None }

        data = self.parser.parse_args()
        try:
            account = Account.query.filter_by(email=data['email']).first()

            if not account.is_hash_match(data['password']):
                raise 'Bad Password'
        except:
            return responze, 404

        responze['user'] = account_schema.dump(account)
        responze['token'] = create_access_token(
                                str(account.id), 
                                expires_delta=datetime.timedelta(minutes=59)
                            )
        return responze


## log a user out
class AccountLogout(Resource):

    @jwt_required
    def post(self):
        responze = { 'logged_out': False }
        return responze
