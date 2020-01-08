## imports
from datetime import datetime

from app import db



class Contact(db.Model):
    id = db.Column( db.Integer, unique=True, primary_key=True )
    account = db.Column( db.String(80), unique=False, nullable=False )
    name = db.Column( db.String(80), unique=True, nullable=False )
    email = db.Column( db.String(80), unique=True, nullable=False )
    phone = db.Column( db.String(12), unique=True, nullable=False )
    added_on = db.Column( db.DateTime, default=datetime.utcnow )

    ## set table name
    __tablename__ = 'contacts'

    def __repr__(self):
        return 'account >> {0}'.format(self.name)

