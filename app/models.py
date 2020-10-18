from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declared_attr
import sqlalchemy as sa

migrate = Migrate()


class IdModel(object):
    @declared_attr
    def id(cls):
        for base in cls.__mro__[1:-1]:
            if getattr(base, "__table__", None) is not None:
                type = sa.ForeignKey(base.id)
                break
        else:
            type = sa.Integer

        return sa.Column(type, primary_key=True)


db = SQLAlchemy(model_class=IdModel)


class NameDescriptionMixin(object):
    name = db.Column(db.String(128))
    description = db.Column(db.Text())


class Skill(db.Model, NameDescriptionMixin):
    core = db.Column(db.Boolean())
    profession_id = db.Column(db.ForeignKey("profession.id"))


class SkillLevel(db.Model):
    skill_id = db.Column(db.ForeignKey("skill.id"))
    assessment_id = db.Column(db.ForeignKey("assessment.id"))
    value = db.Column(db.Integer())


class Profession(db.Model, NameDescriptionMixin):
    pass


class Role(db.Model):
    title = db.Column(db.String(128))

    profession_id = db.Column(db.ForeignKey("profession.id"))


class Posting(db.Model):
    candidate_id = db.Column(db.ForeignKey("candidate.id"))
    role_id = db.Column(db.ForeignKey("role.id"))

    date_started = db.Column(db.Date())
    date_ended = db.Column(db.Date())
    rotation_number = db.Column(db.Integer())


class Assessment(db.Model):
    posting_id = db.Column(db.ForeignKey("posting.id"))

    date = db.Column(db.Date())
    overall_mark = db.Column(db.String(56))

    posting = db.relationship("Posting")

    def candidate(self):
        return Candidate.query.get(self.posting.candidate_id)


class Candidate(db.Model):
    name = db.Column(db.String(128), nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    secondary_email_address = db.Column(db.String(120), unique=True)
    joining_date = db.Column(db.Date(), nullable=False)
    location_restriction = db.Column(
        db.Boolean(), default=False, nullable=False
    )  # TRUE: yes, FALSE: no, NULL: Prefer not to say

    def __repr__(self):
        return f"<Candidate email {self.email_address}>"

    def update_email(self, new_address: str, primary: bool):
        if primary:
            self.email_address = new_address
        elif not primary:
            self.secondary_email_address = new_address

    def current_skill_level(self):
        pass

    def latest_assessment(self):
        pass
