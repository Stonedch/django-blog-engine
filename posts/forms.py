from django import forms
from django.core.exceptions import ValidationError

from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

        widgets = {
            "title": forms.TextInput(),
            "content": forms.Textarea(),
            "tags": forms.SelectMultiple(),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["title", "slug"]

    def clean_slug(self):
        slug = self.cleaned_data["slug"].lower()
        if (not self.instance.id) and (Tag.objects.filter(slug__iexact=slug).count()):
            raise ValidationError("Слаг \"{}\" уже существует.".format(slug.lower()))
        return slug