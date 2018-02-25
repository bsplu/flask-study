from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,ValidationError,length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=4,max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    def validate_username(self, field):
        if field.data != 'usernam12345':
            raise ValidationError('user not existed')
    def validate_password(self, field):
        if field.data != '12345':
            raise ValidationError('wrong password')
