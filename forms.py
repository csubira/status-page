from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField, SubmitField, SelectField, TextAreaField
from wtforms.validators import Required, Length
class StatusForm(Form):
    status = SelectField('Status',choices=[(0, 'Downtime'), (1, 'Uptime'), (2, 'Partial degradation')])
    message = TextAreaField('Message', validators = [ Length(1, 64)])
    submit = SubmitField('Save Status')
