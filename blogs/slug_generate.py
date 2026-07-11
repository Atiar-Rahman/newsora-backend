from django.utils.text import slugify

def generate_unique_slug(model, instance, title_field="title"):
    value = getattr(instance, title_field)
    slug = slugify(value)
    unique_slug = slug
    counter = 1

    queryset = model.objects.filter(slug=unique_slug)

    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    while queryset.exists():
        unique_slug = f"{slug}-{counter}"
        counter += 1
        queryset = model.objects.filter(slug=unique_slug)

    return unique_slug