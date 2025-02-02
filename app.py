from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

site=Flask(_name_)
site.config['SQLALCHEMY_DATABASE_URI']='sqlite:///foods.db'
site.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(site)


class Food(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    cooking_time=db.Column(db.Integer,nullable=False)


with app.app_context():
    db.create_all()
