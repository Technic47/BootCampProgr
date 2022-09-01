from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('SecondName', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Submit')
