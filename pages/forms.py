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

class CreateItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('category',
                  'name',
                  'item_description',
                  'min_order',
                  'min_price',
                  'max_price',
                  'title',
                  'description',
                  'keywords',)

class UpdateItemImageForm(ModelForm):
    class Meta:
        model = ItemImage
        fields = ('image',)


class CreateItemImageForm(ModelForm):
    class Meta:
        model = ItemImage
        fields = ('image','item')

class CreateSliderImageForm(ModelForm):
    class Meta:
        model = AboutSlider
        fields = ('image',)

class UpdateSliderImageForm(ModelForm):
    class Meta:
        model = AboutSlider
        fields = ('id','image',)

class CreateTempImageForm(ModelForm):
    class Meta:
        model = TempImages
        fields = ('image',)