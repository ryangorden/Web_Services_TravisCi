from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask app, load configuration, and
# create the SQLAlchemy object

app= Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///network.db'

db= SQLAlchemy(app)

# This is the database model object

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key=True)
    hostname= db.Column(db.String(120), index=True)
    vendor= db.Column(db.String(40))

    def __init__(self,hostname,vendor):
        self.hostname= hostname
        self.vendor= vendor

    def __repr__(self):
        return '<Device %r>' % self.hostname
        #return f'<Device {self.hostname}>'

if __name__ == '__main__':
    r1 = Device('vpn-router', 'Cisco')
    r2 = Device('mpls-core-router', 'Aruba')
    db.session.add(r1)
    db.session.add(r2)
    db.session.commit()
