import datetime
from werkzeug.security import check_password_hash

from app import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column( db.String(80), unique=True, nullable=False )
    email = db.Column( db.String(80), unique=True, nullable=False )
    password = db.Column( db.String(180), required=True, unique=True )
    joined_on = db.Column( db.DateTime, default=datetime.datetime.utcnow )

    ## set collection name
    __tablename__ = 'accounts' 

    def __repr__(self):
        return 'im {0} and my email is {1}'.format(self.name, self.email)


    ''' check if a password matches with this objects hashed password '''
    def is_hash_match(self, password):
        return check_password_hash(self.password, password)

    ''' check if name is used '''
    def name_used(self):
        matches = self.query.filter_by(name=self.name).first()
        return len(matches) > 0
    
    ''' check if email is used '''
    def email_used(self):
        matches = self.query.filter_by(email=self.email).first()
        return len(matches) > 0
