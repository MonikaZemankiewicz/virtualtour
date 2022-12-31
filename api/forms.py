from django import forms
from .models import Image, Video


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = [
            'title',
            'description',
            'image',
            'tags',
        ]
