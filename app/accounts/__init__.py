from flask import Blueprint
from flask_restful import Api


## import schemas and models
from .models import Account
from .schemas import (
    AccountSchema, account_schema, accounts_schema
)


## create accounts blueprint
accounts_bp = Blueprint('accounts_bp', __name__)
## create accounts api
accounts_api = Api(accounts_bp)

## import resources
from .resources import (
    AccountCreate, AccountDelete, AccountDesignate,
    AccountUpdate, AccountAppointments, AccountBusinesses,
    AccountDetails, AccountNameOrEmailUsed, AccountUpdatePassword,
    AccountLogin, AccountLogout  
)

## add resources to blueprint
accounts_api.add_resource(AccountCreate, '/')
accounts_api.add_resource(AccountDetails, '/<id>')
accounts_api.add_resource(AccountUpdate, '/<id>')
accounts_api.add_resource(AccountUpdatePassword, '/<id>/password')
accounts_api.add_resource(AccountNameOrEmailUsed, '/name-or-email/used')
accounts_api.add_resource(AccountDelete, '/<id>')
accounts_api.add_resource(AccountLogin, '/login')
accounts_api.add_resource(AccountLogout, '/logout')


@accounts_bp.route('/')
def index():
    return { 'index': 'accounts_bp content' }