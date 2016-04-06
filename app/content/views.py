# -*- coding:utf-8 -*-

from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, \
    current_user
from .models import Catalog,Content
from . import content
from .forms import CatalogForm
from .. import db

@content.route("/catalogs", methods=['GET', 'POST'])
@login_required
def catalogs():
    catalogs=Catalog.query.all()
    return render_template("content/catalogs.html",catalogs=catalogs)


@content.route("/add_catalog", methods=['GET', 'POST'])
@login_required
def add_catalog():
    form=CatalogForm()
    if form.validate_on_submit():
        catalog=Catalog(name=form.name.data,description=form.description.data);
        db.session.add(catalog)
        db.session.commit()
        flash(u'目录保存成功')
        return redirect(url_for('content.catalogs'))
    return render_template('content/catalog.html', form=form)

@content.route("/delete_catalog/<int:catalog_id>", methods=['GET'])
@login_required
def delete_catalog(catalog_id):
    if catalog_id:
        catalog=Catalog.query.get(catalog_id)
        if catalog:
            db.session.delete(catalog)
            db.session.commit()
            flash(u'删除成功！')
        else:
            flash(u'找不到要删除的目录！','error')
    else:
        flash(u'找不到要删除的目录！','error')
    return redirect(url_for('content.catalogs'))
@content.route("/edit_catalog/<int:catalog_id>", methods=['GET','POST'])
@login_required
def edit_catalog(catalog_id):
    catalog=Catalog.query.get_or_404(catalog_id)
    form=CatalogForm()
    if form.validate_on_submit():
        catalog.name=form.name.data
        catalog.description=form.description.data
        flash(u'目录修改成功！')
        return redirect(url_for('content.catalogs'))
    form.name.data=catalog.name
    form.description.data=catalog.description
    return render_template('content/catalog.html', form=form)
