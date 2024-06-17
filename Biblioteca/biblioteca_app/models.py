from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    image_url = models.URLField(max_length=200, blank=True, null=True)  # Nuevo campo

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200, blank=True, null=True)  # Nuevo campo

    def __str__(self):
        return self.title
