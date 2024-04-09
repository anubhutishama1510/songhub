from django.db import models

class MyModel(models.Model):
    filelocation = models.FileField(upload_to='uploads/')  
