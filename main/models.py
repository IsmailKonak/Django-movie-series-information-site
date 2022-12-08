from django.db import models
from django.contrib.auth import get_user_model

class Star(models.Model):
    star_name = models.CharField(max_length=500)

    def __str__(self):
        return self.star_name

class Categorie(models.Model):
    category = models.CharField(max_length=300)

    def __str__(self):
        return self.category


class Movie(models.Model):
    User_db = get_user_model()

    poster = models.FileField(null=True, blank=True, upload_to="movies/")
    name = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    distribution = models.CharField(max_length=200)
    release = models.DateField(max_length=200)
    summary = models.TextField(max_length=2000,null=True)
    
    user = models.ForeignKey(User_db, null=True, on_delete=models.CASCADE)
    star = models.ManyToManyField(Star, blank=True)
    categorie = models.ManyToManyField(Categorie, blank=True)
    url_name = models.CharField(max_length=500,null=True)

    def __str__(self):
        return self.name

    def getcontenttype(self):
        return "Movie"

class Series(models.Model):
    User_db = get_user_model()

    poster = models.FileField(null=True, blank=True, upload_to="series/")
    name = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    distribution = models.CharField(max_length=200)
    release = models.DateField(max_length=200)
    summary = models.TextField(max_length=2000,null=True)

    user = models.ForeignKey(User_db, null=True, on_delete=models.CASCADE)
    star = models.ManyToManyField(Star, blank=True)
    categorie = models.ManyToManyField(Categorie, blank=True)
    url_name = models.CharField(max_length=500,null=True)


    def __str__(self):
        return self.name

    def getcontenttype(self):
        return "Series"
