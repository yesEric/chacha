# -*- coding:utf-8 -*-

from flask import current_app
from .. import db
from ..models import Base
from ..models import User
from datetime import datetime


class Catalog(Base):
    __tablename__='catalogs'
    name = db.Column(db.String(64), unique=True)
    description=db.Column(db.String(255),unique=False)

    def __repr__(self):
        return '<Catalog %r>' % self.name

    def __init__(self,name,description):
        self.name=name
        self.description=description

class Content(Base):
    __tablename__='contents'
    title=db.Column(db.String(64),unique=False)
    body_text=db.Column(db.String(255))
    catalog_id=db.Column(db.Integer,db.ForeignKey("catalogs.id"))
    catalog=db.relationship("Catalog",backref="contents")
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    user=db.relationship("User",backref="contents")
    created_at=db.Column(db.DateTime)

    def __repr__(self):
        return '<Content %r>' % self.title

    def __init__(self,title,body_text,catalog,user):
        self.title=title
        self.body_text=body_text
        self.catalog=catalog
        self.user=user
        self.created_at=datetime.now()


def find_users_contents(user_id):
    return Content.query.filter_by(created_by=user_id)