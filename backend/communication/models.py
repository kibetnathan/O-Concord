from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    image = CloudinaryField