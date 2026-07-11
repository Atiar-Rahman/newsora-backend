from django.db import models
from core.models import BaseModel
from blogs.slug_generate import generate_unique_slug

class Category(BaseModel):
    title = models.CharField(max_length=150, unique=True, db_index=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="categories/", null=True, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Category, self)

        super().save(*args, **kwargs)


class Tag(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Tag, self)

        super().save(*args, **kwargs)


class Blog(BaseModel):
    DRAFT = "draft"
    PUBLISHED = "published"

    STATUS = (
        (DRAFT, "Draft"),
        (PUBLISHED, "Published"),
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="blogs"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="blogs"
    )

    tags = models.ManyToManyField(
        Tag,
        related_name="blogs",
        blank=True
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    short_description = models.CharField(max_length=300)

    description = models.TextField()

    image = models.ImageField(
        upload_to="blogs/",
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS,
        default=DRAFT
    )
    location = models.CharField(max_length=200)

    is_featured = models.BooleanField(default=False)

    views = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)

    published_at = models.DateTimeField(
        null=True,
        blank=True
    )

    # SEO
    meta_title = models.CharField(
        max_length=255,
        blank=True
    )

    meta_description = models.CharField(
        max_length=300,
        blank=True
    )

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(Blog, self)

        super().save(*args, **kwargs)