from django.forms import ModelForm

from .models import Forms



class CreateForm(ModelForm):
     class Meta:
        model = Forms
        fields = (
            'name',
            'phone',
            'email',
            'file',
        )
