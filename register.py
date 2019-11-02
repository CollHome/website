from sqlalchemy import Column, Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

import re

Base = declarative_base()

class Chapter(Base):
    __tablename__ = "Chapters"
    id = Column(Integer, primary_key=True)
    university = Column(String)
    location = Column(String)
    contactname = Column(String)
    chapteremail = Column(String)
    founderemails = Column(String)

emailregex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class Register(FlaskForm):
    university = StringField("Name of University", validators=[DataRequired()])
    location = StringField("University Location", validators=[DataRequired()])
    contactname = StringField("Name of Primary Contact", validators=[DataRequired()])
    chapteremail = StringField("Public Chapter Email", validators=[DataRequired()])
    founderemails = StringField("Emails of Founding Chapter Members (Separate with commas)")
    submit = SubmitField("Submit")

    def validate_chapteremail(form, field):
        if not emailregex.fullmatch(field.data):
            raise ValidationError("Chapter Email must be a valid email address!")
