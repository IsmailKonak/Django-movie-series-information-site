from django import forms
from main.models import Movie, Series 

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ["poster", "name","director", "writer","distribution","release", "summary"]
        exclude= ["user","star","categorie"]

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ["poster", "name","director", "writer","distribution","release", "summary"]
        exclude= ["user","star","categorie"]

