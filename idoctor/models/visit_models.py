from idoctor import db


class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_visit = db.Column(db.DateTime, nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.id"), nullable=False)

    @staticmethod
    def get_visit_all():
        return Visit.query.all()

