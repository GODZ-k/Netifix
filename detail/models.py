from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Categories(models.Model):
    category=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category

class movie(models.Model):
    category=models.ForeignKey(Categories,related_name="categories", on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    description=models.TextField()
    imdb_rating=models.FloatField()
    movie_duration=models.CharField(max_length=20)
    movie_year=models.IntegerField()
    movie_trailler=models.CharField(max_length=200)
    movie_match=models.CharField(max_length=100)
    movie_grade=models.CharField(max_length=200)
    poster_portrait=models.ImageField(upload_to="movie_media")
    director=models.CharField(max_length=200)
    distibuted_by=models.CharField(max_length=200)
    cast=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    quality=models.CharField(max_length=200)
    screenshot_1=models.ImageField(upload_to="movie_media")
    screenshot_2=models.ImageField(upload_to="movie_media")
    screenshot_3=models.ImageField(upload_to="movie_media")
    screenshot_4=models.ImageField(upload_to="movie_media")
    screenshot_5=models.ImageField(upload_to="movie_media")
    screenshot_6=models.ImageField(upload_to="movie_media")
    slug=AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    title=models.CharField(max_length=300)
    released_at=models.DateField(null=True , blank=True)
    updated_at=models.DateTimeField(auto_now=True)

class trending(models.Model):
    poster_landscape=models.ImageField(upload_to="movie_media")
    movies=models.ForeignKey(movie, related_name="trending_movies", on_delete=models.CASCADE)

class hot_thrills(models.Model):
    movies=models.ForeignKey(movie, related_name="hot_thrills_movies", on_delete=models.CASCADE)
    update=models.CharField(max_length=100)
    label=models.CharField(max_length=200)
    clip=models.FileField(upload_to="movie_media")

class poster(models.Model):
    movie_wallpaper=models.ImageField(upload_to="movie_media")
    movies=models.ForeignKey(movie, related_name="poster_movies", on_delete=models.CASCADE)

