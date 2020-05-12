from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request 
from flask import url_for
from flask import redirect
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy import Column, ForeignKey, Integer, String, BOOLEAN, ARRAY
import json

app1= Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0567@localhost/fyyur1'
app1.debug=True
db = SQLAlchemy(app1)


class Artist(db.Model):
    __tablename__ = 'Artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state= db.Column(db.String(120))
    phone = db.Column(db.String(120), unique=True)
    genres = db.Column(db.String(120))
    facbook_link = db.Column(db.String(120), unique=True)
    photo = db.Column(db.String(500),default='default.jpg')
    seeking__description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='Artist', lazy=True)


    def __repr__(self):
        return '<Artist %r>' % self.name , self.city , self.state , self.phone ,self.photo, self.genres , self.facbook_link , self.seeking__description
    
    def __init__(self , name , city,state , phone , genres, facbook_link,seeking__description):
          self.name =name
          self.city=city
          self.state=state
          self.phone=phone
          self.genres=genres
          self.facbook_link=facbook_link
          self.seeking__description=seeking__description
          self.photo=photo

class Venue(db.Model):
    __tablename__ = 'Venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    address = db.Column(db.String(500))
    phone = db.Column(db.String(120), unique=True)
    genres = db.Column(db.String(120))
    facbook_link = db.Column(db.String(120), unique=True)
    photo = db.Column(db.String(120),default='default.jpg')
    shows=db.relationship('Show',backref='owner')






class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey(Artist.id), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey(Venue.id), nullable=False)

   
    def __repr__(self):
        return f'<Show ID:{self.id}, start_time: {self.start_time}>'

    @app1.route("/post_Artist", methods=['POST'])
    def Artist_create():
       artist = Artist(request.form['name'], request.form['city'], request.form['state'], request.form['phone'], request.form['genres'], request.form['facbook_link'], request.form['seeking__description'], )
       db.session.add(artist)
       db.session.commit()
       return redirect(url_for(index))

@app1.route("/")
def index():
	return render_template('pages/HTMLPage1.html')


if __name__ =="__main__":
    app1.run()
