from django.db import models

# Create your models here.

# class categories(models.model):


class movie(models.model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    imdb_rating=models.FloatField()
    movie_duration=models.CharField(max_length=20)
    movie_year=models.IntegerField()
    movie_trailler=models.CharField(max_length=200)
    movie_match=models.CharField(max_length=100)
    movie_grade=models.CharField(max_length=200)
    poster_portrait=models.ImageField(upload_to="movie_images")
    poster_landscape=models.ImageField(upload_to="movie_images")


    released_at=models.DateField(null=True , blank=True)
    updated_at=models.DateTimeField(auto_now=True)



class hot_thrills(models.Model):
