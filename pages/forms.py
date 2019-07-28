from django.forms import ModelForm

from .models import *



class CreateForm(ModelForm):
     class Meta:
        model = Forms
        fields = (
            'name',
            'phone',
            'email',
            'file',
        )


class AboutClientsForm(ModelForm):
    class Meta:
        model = AboutPageClients
        fields = (
            'image',

        )

class AboutWorkForm(ModelForm):
    class Meta:
        model = AboutPageWork
        fields = (
            'image',

        )



class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'image',
            'title',
            'description',
            'keywords',)

class CategoryUpdateForm(ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'image',
            'title',
            'description',
            'keywords',)