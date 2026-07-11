from django.db import models
from core.models import BaseModel
from blogs.models import Blog

# Create your models here.
class Comment(BaseModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comments"
    )

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="comments"
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies"
    )

    comment = models.TextField()

    is_approved = models.BooleanField(default=True)

    likes_count = models.PositiveIntegerField(default=0)
    replies_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user} - {self.blog.title}"


class BlogReaction(BaseModel):
    LIKE = "like"
    DISLIKE = "dislike"

    REACTIONS = (
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="blog_reactions"
    )

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="reactions"
    )

    reaction = models.CharField(
        max_length=10,
        choices=REACTIONS
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "blog"],
                name="unique_blog_reaction"
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.blog}"


class CommentReaction(BaseModel):
    LIKE = "like"
    DISLIKE = "dislike"

    REACTIONS = (
        (LIKE, "Like"),
        (DISLIKE, "Dislike"),
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comment_reactions"
    )

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="reactions"
    )

    reaction = models.CharField(
        max_length=10,
        choices=REACTIONS
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "comment"],
                name="unique_comment_reaction"
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.comment.id}"


class Bookmark(BaseModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="bookmarks"
    )

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="bookmarks"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "blog"],
                name="unique_bookmark"
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.blog}"


class BlogView(BaseModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="blog_views"
    )

    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="view_logs"
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    user_agent = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.blog.title


class Subscriber(BaseModel):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
    