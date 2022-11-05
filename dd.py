from app.extensions import db
from app.users.model import User
from app.posts.model import Post
from datetime import datetime
import bcrypt

#

def create_dd(app):
    with app.app_context():
        db.create_all()
        db.session.commit()

        if not User.query.first():
            user = User(name="Pedro Rocha",
                                email="pedro.rocha1980@gmail.com",
                                pw_hash=bcrypt.hashpw("senha456".encode(), bcrypt.gensalt()))
            

            db.session.add(user)
            db.session.commit()

        db.session.commit()
               