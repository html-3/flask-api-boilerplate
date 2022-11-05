from app.utils.base import BaseModel
from app.extensions import db


class Post(BaseModel):

    title = db.Column(db.String(200), unique=True)
    content = db.Column(db.Text, unique=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
