from django import forms
from django.contrib.auth.models import User
from .models import Video

class Video_form(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('caption', 'video')