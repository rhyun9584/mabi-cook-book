from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    EmailField,
    SelectField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    EqualTo,
    Email,
    ValidationError,
)

from app.models import User


class UserCreateForm(FlaskForm):
    email = EmailField('이메일 ID')
    password1 = PasswordField('비밀번호')
    password2 = PasswordField('비밀번호 확인')
    server = SelectField('서버', choices=['류트', '하프', '울프', '만돌린'])
    name = StringField('닉네임')


class UserSigninForm(FlaskForm):
    email = EmailField('이메일 ID')
    password = PasswordField('비밀번호')


class ChangePwForm(FlaskForm):
    old_pw = PasswordField('현재 비밀번호')
    new_pw1 = PasswordField('새 비밀번호')
    new_pw2 = PasswordField('새 비밀번호 확인')


class SearchPwForm(FlaskForm):
    email = EmailField('이메일 ID')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('존재하지 않는 이메일 ID입니다.')


class ResetPwForm(FlaskForm):
    new_pw1 = PasswordField('새 비밀번호')
    new_pw2 = PasswordField('새 비밀번호 확인')


class LeaveForm(FlaskForm):
    password = PasswordField('비밀번호')
