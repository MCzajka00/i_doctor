from idoctor import db


class Clinic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    @staticmethod
    def get_clinics():
        return Clinic.query.all()
