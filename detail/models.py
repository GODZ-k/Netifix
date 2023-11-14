from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Categories(models.Model):
    category=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category

    class Meta:
        verbose_name_plural = 'Categories'

class movie(models.Model):
    category=models.ManyToManyField(Categories,related_name="categories")
    name=models.CharField(max_length=50)
    description=models.TextField()
    imdb_rating=models.FloatField()
    movie_duration=models.CharField(max_length=20)
    movie_year=models.IntegerField()
    movie_trailler=models.CharField(max_length=200)
    movie_match=models.CharField(max_length=100)
    movie_grade=models.CharField(max_length=200)
    poster_portrait=models.URLField(max_length=900)
    director=models.CharField(max_length=200)
    distibuted_by=models.CharField(max_length=200)
    cast=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    quality=models.CharField(max_length=200)
    screenshot_1=models.URLField(max_length=900)
    screenshot_2=models.URLField(max_length=900)
    screenshot_3=models.URLField(max_length=900)
    screenshot_4=models.URLField(max_length=900)
    screenshot_5=models.URLField(max_length=900)
    screenshot_6=models.URLField(max_length=900)
    slug=AutoSlugField(populate_from='movie_title',unique=True,null=True,default=None)
    movie_title=models.CharField(max_length=300)
    released_at=models.DateField(null=True , blank=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Add movies'

class trending(models.Model):
    poster_landscape=models.URLField(max_length=900)
    movies=models.ForeignKey(movie, related_name="trending_movies", on_delete=models.CASCADE)

    def __str__(self) ->str:
        return self.movies.name

    class Meta:
        verbose_name_plural = 'Trending Silder'

class hot_thrills(models.Model):
    movies=models.ForeignKey(movie, related_name="hot_thrills_movies", on_delete=models.CASCADE)
    # update=models.CharField(max_length=100)
    label=models.CharField(max_length=200)
    clip=models.FileField(upload_to="movie_media")

    def __str__(self) -> str:
        return self.movies.name

    class Meta:
        verbose_name_plural = 'Hot Slideshow'

class poster(models.Model):
    movie_wallpaper=models.ImageField(upload_to="movie_media")
    movies=models.ForeignKey(movie, related_name="poster_movies", on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.movies.name

    class Meta:
        verbose_name_plural = 'Recommanded posters'

