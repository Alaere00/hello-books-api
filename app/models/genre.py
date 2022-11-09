from app import db
class Genre(db.Model):
    genre_id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String)
