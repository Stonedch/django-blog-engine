from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


def gen_slug(line):
    slug = slugify(line, allow_unicode=True)
    return slug


class Post(models.Model):
    title = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, unique=True)
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")
    content = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_detail_url", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("post_update_url", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("post_delete_url", kwargs={"slug": self.slug})

    def __str__(self):
        return "{}".format(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, unique=True)

    def get_absolute_url(self):
        return reverse("tag_detail_url", kwargs={"slug": self.slug})

    def get_update_url(self):
        return reverse("tag_update_url", kwargs={"slug": self.slug})

    def get_delete_url(self):
        return reverse("tag_delete_url", kwargs={"slug": self.slug})

    def __str__(self):
        return "{}".format(self.title)