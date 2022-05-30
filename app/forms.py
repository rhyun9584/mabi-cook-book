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
    email = EmailField('이메일 ID', validators=[DataRequired(), Email()])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.'), Length(min=6)])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    server = SelectField('서버', choices=['류트', '하프', '울프', '만돌린'])
    name = StringField('닉네임', validators=[DataRequired()])


class UserSigninForm(FlaskForm):
    email = EmailField('이메일 ID', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired()])


class ChangePwForm(FlaskForm):
    old_pw = PasswordField('현재 비밀번호', validators=[DataRequired()])
    new_pw1 = PasswordField('새 비밀번호', validators=[DataRequired(),
                                                  EqualTo('new_pw2', '비밀번호가 일치하지 않습니다.'), Length(min=6)])
    new_pw2 = PasswordField('새 비밀번호 확인', validators=[DataRequired()])


class SearchPwForm(FlaskForm):
    email = EmailField('이메일 ID', validators=[DataRequired(), Email()])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('존재하지 않는 이메일 ID입니다.')


class ResetPwForm(FlaskForm):
    new_pw1 = PasswordField('새 비밀번호', validators=[DataRequired(),
                                                  EqualTo('new_pw2', '비밀번호가 일치하지 않습니다.'), Length(min=6)])
    new_pw2 = PasswordField('새 비밀번호 확인', validators=[DataRequired()])
