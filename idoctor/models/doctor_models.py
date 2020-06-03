from idoctor import db


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    duration_visit = db.Column(db.Time)
    visit = db.relationship('Visit', backref='doctor', lazy='dynamic')

    @staticmethod
    def get_doctors():
        return Doctor.query.all()
