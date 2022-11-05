from app.extensions import ma
from posts.model import Post
from marshmallow import EXCLUDE, post_dump, pre_load, validates
from flask import make_response

class PostSchema(ma.SQLALchemy):
    class Meta:
        model = Post
        load_instance = True
        ordered = True
        unknown = EXCLUDE
        strict = False

    id =  ma.Integer(dump_only=True)
    
    title = ma.String(required=True)
    content = ma.String(required=True)

    updated_at  = ma.DateTime(dump_only=True) 
    created_at  = ma.DateTime(dump_only=True) 
    
    @pre_load 
    def pre_check(self, data, **kwargs):
        return data

    @validates("title") 
    def validate_title(self, title : str):
        # Zero length title
        if len(title) == title.count(" ") or len(title) >= 100:
            make_response(400, "Invalid title length, should be between 0 and 100")

    @validates("content") 
    def validate_content(self, content : str):
        # Zero length content
        if len(content) == content.count(" ") or len(content) >= 100:
            make_response(400, "Invalid content length, should be between 0 and 100")