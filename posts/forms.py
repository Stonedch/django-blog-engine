from django import forms
from django.core.exceptions import ValidationError

from .models import Tag

class TagForm(forms.Form):
    title = forms.CharField(max_length=128)
    slug = forms.SlugField(max_length=128)

    def clean_slug(self):
        slug = self.cleaned_data["slug"].lower()
        if Tag.objects.filter(slug__iexact=slug).count():
            raise ValidationError("Слаг \"{}\" уже существует.".format(slug.lower()))
        return slug

    def save(self):
        tag = Tag.objects.create(title=self.cleaned_data["title"],
                                 slug=self.cleaned_data["slug"])
        return tag