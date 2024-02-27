from datetime import datetime

from django.utils.text import slugify
from ninja import Router, Schema

from blog.models import Comment, Post, User

router = Router()


class UserIn(Schema):
    username: str
    password: str


class UserOut(Schema):
    id: int
    username: str


class PostIn(Schema):
    title: str
    body: str


class AuthorOut(Schema):
    username: str


class PostOut(Schema):
    title: str
    slug: str
    body: str
    author: AuthorOut
    created: datetime


class CommentIn(Schema):
    post_id: int
    body: str


class CommentOut(Schema):
    post_id: int
    user_id: int
    body: str
    created: datetime
    user: AuthorOut


@router.post("/users/", response=UserOut)
def create_user(request, data: UserIn):
    user = User.get(username=data.username)
    user.set_password(data.password)
    return user


@router.get("/comments/{post_id}", response=list[CommentOut])
def comment_list(request, post_id: int):
    post = Post.objects.get(id=post_id)
    return post.comments.select_related("user")


@router.post("/comments/", response=CommentOut)
def comment_create(request, payload: CommentIn):
    values = payload.dict()
    values["user_id"] = int(request.user.id)
    comment = Comment.objects.create(**values)
    comment.save()
    return comment


@router.get("/", response=list[PostOut])
def post_list(request):
    return Post.approved.select_related("author").all()


@router.get("/{post_id}", response=PostOut)
def post_detail(request, post_id: int):
    return Post.objects.get(id=post_id)


@router.post("/")
def post_create(request, payload: PostIn):
    values = payload.dict()
    values["author_id"] = int(request.user.id)
    values["slug"] = slugify(values["title"])
    post = Post.objects.create(**values)
    post.save()
    return {"id": post.id}
