from app import ma 
from marshmallow import fields


class AccountSchema(ma.Schema):
    fields = ( 'id', 'name', 'email', 'joined_on', 'account_type' )


account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)