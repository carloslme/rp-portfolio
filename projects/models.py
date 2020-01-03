from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100) # will be a short string field to hold the name of your project.
    description = models.TextField() # will be a larger string field to hold a longer piece of text.
    technology = models.CharField(max_length=20) # will be a string field, but its contents will be limited to a select number of choices.
    image = models.FilePathField(path="/img") #  will be an image field that holds the file path where the image is stored.
