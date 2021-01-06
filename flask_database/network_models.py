from Network_Database import db

# This is the database model object
class Device(db.Model):
    __tablename__ = 'devices'
    id= db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(80), unique=True)
    vendor = db.Column(db.String(120), unique=True)

    def __init__(self, hostname, vendor):
        self.hostname = hostname
        self.vendor = vendor

    def __repr__(self):
        return f'<Device {self.hostname}>'

if __name__ == '__main__':
    db.create_all()
    r1 = Device('vpn-router', 'Cisco')
    r2 = Device('mpls-core-router', 'Aruba')
    # db.session.add(r1)
    # db.session.add(r2)
    # db.session.commit()
    print(Device.query.all())
    # print(Device.query.filter_by(hostname='vpn-router'))