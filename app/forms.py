from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    EmailField
)
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserCreateForm(FlaskForm):
    email = EmailField('이메일 ID', validators=[DataRequired(), Email()])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.'), Length(min=6)])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    name = StringField('닉네임', validators=[DataRequired()])


class UserSigninForm(FlaskForm):
    email = EmailField('이메일 ID', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])