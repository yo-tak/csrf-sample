from app import db


class Purchases(db.Model):
    __tablename__ = 'purchases'
    username = db.Column(db.String(40), primary_key=True)
    count = db.Column(db.Integer)

    def __repr__(self):
        return '<Purchases username={username} count={count}'.format(username=self.username, count=self.count)


class Accounts(db.Model):
    __tablename__ = 'accounts'
    username = db.Column(db.String(40), primary_key=True)
    password = db.Column(db.String(64))

    def __repr__(self):
        return '<Accounts username={username}'.format(username=self.username)
    # ----------------------------------------------------------------------


def init():
    db.create_all()
