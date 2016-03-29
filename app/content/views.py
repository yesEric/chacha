# -*- coding:utf-8 -*-

from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, \
    current_user
from .models import Catalog,Content
from . import content


@content.route("/catalogs", methods=['GET', 'POST'])
@login_required
def catalogs():
    catalogs=Catalog.query.all()
    return render_template("content/catalogs.html",catalogs=catalogs)