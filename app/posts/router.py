from flask import Blueprint
from app.posts.controller import PostGeneral, PostSpecific

post_router = Blueprint("post_router", __name__)

post_router.add_url_rule(
    "/posts",
    view_func=PostGeneral.as_view("posts"), 
    methods = ["GET", "POST"]
)

post_router.add_url_rule(
    "/post/<int:post_id>",
    view_func=PostSpecific.as_view("post"), 
    methods = ["GET", "UPDATE", "DELETE"]
)