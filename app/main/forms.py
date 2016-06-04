from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import required


class NameForm(Form):
    name = StringField("What's your name?", validators=[required()])
    submit = SubmitField("Submit")


