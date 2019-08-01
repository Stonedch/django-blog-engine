from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import *

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template,
                      context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={"form": form})
    
    def post(self, request):
        form = self.form_model(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(obj)
        return render(request, self.template, context={"form": form})


class ObjectUpdateMixin:
    model = None
    form_model = None
    template = None

    def get(self, request, slug):
        updatable_model = self.model.objects.get(slug__iexact=slug)
        updatable_form = self.form_model(instance=updatable_model)
        return render(request, self.template, context={"form": updatable_form})
    
    def post(self, request, slug):
        updatable_model = self.model.objects.get(slug__iexact=slug)
        updatable_form = self.form_model(request.POST, instance=updatable_model)
        if updatable_form.is_valid():
            updated_form = updatable_form.save()
            return redirect(updated_form)
        return render(request, self.template, context={"form": updatable_form})


class ObjectDeleteMixin:
    model = None
    template = None
    reverse_url = None

    def get(self, request, slug):
        deletable_model = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template,
                      context={self.model.__name__.lower(): deletable_model})
    
    def post(self, request, slug):
        deletable_model = self.model.objects.get(slug__iexact=slug)
        deletable_model.delete()
        return redirect(reverse(self.reverse_url))