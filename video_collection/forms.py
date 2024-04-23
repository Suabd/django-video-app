from django import forms
from .models import Video

# this is for adding video
class videoForm(forms.ModelForm):
    class Meta:
        model = Video 
        fields = ['name', 'url', 'notes']

# this is form for serching video. or allwing to serch video thats in the video_list
class SearchForm(forms.Form):
    search_term = forms.CharField()