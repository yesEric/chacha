# -*- coding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField,SelectField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo, DataRequired
from wtforms import ValidationError
from ..models import User
from .models import Catalog


class CatalogForm(Form):
    name=StringField(u'名称',validators=[DataRequired(), Length(1, 64)])
    description=TextAreaField(u'描述',validators=[Length(0,255)])
    submit = SubmitField(u'保存')

class ContentForm(Form):

    title=StringField(u'标题',validators=[DataRequired(), Length(1, 64)])
    catalog_id=SelectField(u'目录',coerce=int)
    body_text=TextAreaField(u'内容',validators=[Length(0,2550)])
    submit = SubmitField(u'保存')

    def __init__(self, *args, **kwargs):
        super(ContentForm, self).__init__(*args, **kwargs)
        self.catalog_id.choices = [(catalog.id, catalog.name)
                             for catalog in Catalog.query.all()]
