from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')

    def __str__(self):
        return f'{self.user.username} Profile'


    # NOTE: Need to delete old image before adding a new one.
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 256 or img.width > 256:
            output_size = (256, 256)
            img.thumbnail(output_size)

        img.save(self.image.path)
