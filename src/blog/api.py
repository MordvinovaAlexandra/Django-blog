from datetime import datetime

from ninja import Router, Schema

from blog.models import Post

router = Router()


class PostOut(Schema):
    title: str
    slug: str
    body: str
    created: datetime


@router.get("/", response=list[PostOut])
def post_list(request):
    return Post.approved.all()
