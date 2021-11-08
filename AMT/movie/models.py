from django.db import models

# Create your models here.
class movie(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    Name = models.CharField(max_length=30)
    Description = models.TextField(max_length=1000)
    Trailer= models.URLField(max_length=1000)
    WTW1 = models.URLField(blank=True, max_length=1000)
    WTW2 = models.URLField(blank=True, max_length=1000)
    WTW3 = models.URLField(blank=True, max_length=1000)
    WTW4 = models.URLField(blank=True, max_length=1000)
    Poster = models.ImageField(null=True)
    Rate = models.DecimalField(decimal_places=1, max_digits=2)
    MPCR = models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R')], max_length=20)
    Date = models.DateField()
    T9nef =  models.CharField(blank=True, choices=[('Drama', 'Drama'), ('Action', 'Action'), ('Horror', 'Horror'), ('Comedy', 'Comedy'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Animation', 'Animation'), ('Crime', 'Crime'), ('Sci-Fi', 'Sci-Fi'), ('Fantasy', 'Fantasy'), ('Family', 'Family'), ('Thriller', 'Thriller'), ('War', 'War'), ('Documentary', 'Documentary'), ('Music', 'Music'), ('History', 'History'), ('Biography', 'Biography'), ('Sport', 'Sport'), ('Western', 'Western'), ('Political', 'Political')], max_length=20)
    T9nef2 =  models.CharField(blank=True, choices=[('Drama', 'Drama'), ('Action', 'Action'), ('Horror', 'Horror'), ('Comedy', 'Comedy'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Animation', 'Animation'), ('Crime', 'Crime'), ('Sci-Fi', 'Sci-Fi'), ('Fantasy', 'Fantasy'), ('Family', 'Family'), ('Thriller', 'Thriller'), ('War', 'War'), ('Documentary', 'Documentary'), ('Music', 'Music'), ('History', 'History'), ('Biography', 'Biography'), ('Sport', 'Sport'), ('Western', 'Western'), ('Political', 'Political')], max_length=20)
    T9nef3 =  models.CharField(blank=True, choices=[('Drama', 'Drama'), ('Action', 'Action'), ('Horror', 'Horror'), ('Comedy', 'Comedy'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Animation', 'Animation'), ('Crime', 'Crime'), ('Sci-Fi', 'Sci-Fi'), ('Fantasy', 'Fantasy'), ('Family', 'Family'), ('Thriller', 'Thriller'), ('War', 'War'), ('Documentary', 'Documentary'), ('Music', 'Music'), ('History', 'History'), ('Biography', 'Biography'), ('Sport', 'Sport'), ('Western', 'Western'), ('Political', 'Political')], max_length=20)
    T9nef4 =  models.CharField(blank=True, choices=[('Drama', 'Drama'), ('Action', 'Action'), ('Horror', 'Horror'), ('Comedy', 'Comedy'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Animation', 'Animation'), ('Crime', 'Crime'), ('Sci-Fi', 'Sci-Fi'), ('Fantasy', 'Fantasy'), ('Family', 'Family'), ('Thriller', 'Thriller'), ('War', 'War'), ('Documentary', 'Documentary'), ('Music', 'Music'), ('History', 'History'), ('Biography', 'Biography'), ('Sport', 'Sport'), ('Western', 'Western'), ('Political', 'Political')], max_length=20)
    def __str__(self):
        return self.Name
