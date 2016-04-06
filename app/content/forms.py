# -*- coding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo, DataRequired
from wtforms import ValidationError
from ..models import User

class CatalogForm(Form):
    name=StringField(u'名称',validators=[DataRequired(), Length(1, 64)])
    description=TextAreaField(u'描述',validators=[Length(0,255)])
    submit = SubmitField(u'保存')

