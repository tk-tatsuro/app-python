from wtforms.form import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flasklg.models import User


# ログイン画面で利用
class LoginForm(Form):
    email = StringField('メール： ', validators=[DataRequired(), Email()])
    password = PasswordField('パスワード： ', validators=[DataRequired()])
    submit = SubmitField('ログイン')


# 登録画面で利用
class RegisterForm(Form):
    email = StringField('メール： ',validators=[DataRequired, Email()])
    username = StringField('ユーザ名： ',validators=[DataRequired])
    password = PasswordField(
        'パスワード確認： ', validators=[DataRequired(), EqualTo('password_confirm', message='パスワードが一致しません。')]
    )
    password_confirm = PasswordField('パスワード確認 ：', validators=[DataRequired()])
    submit = SubmitField('登録')

    def validate_email(self, field):
        if User.select_by_email(field.data):
            raise ValidationError('メールアドレスが既に登録されています。')


