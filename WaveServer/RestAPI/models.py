from django.db import models
from .common import user_directory_path

# Create your models here.
class WaveUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100, null=True, blank=True)
    create_date = models.DateTimeField(auto_now=True)
    _file = models.FileField(upload_to=user_directory_path, null=True)

    def __str__(self):
        return self.name
