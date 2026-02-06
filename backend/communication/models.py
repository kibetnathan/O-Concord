from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    image = CloudinaryField("image", null=True, blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    tags = TaggableManager()

    def __str__(self):
        return self.title