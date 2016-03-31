from kisios.app import db


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    _balance = db.Column(db.Integer, default=0, nullable=False)

    def get_name(self):
        if self.first_name is not None and self.last_name is not None:
            return self.first_name + ' ' + self.last_name
        elif self.first_name is not None:
            return self.first_name
        elif self.last_name is not None:
            return self.last_name
        else:
            return 'Anonymous customer'

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        raise RuntimeError('Direct manipulation of the balance is forbidden.')
