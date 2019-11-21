from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from math import ceil
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')

    def __str__(self):
        return f'{self.user.username} Profile'


    # NOTE: Need to delete old image before adding a new one.
    def save(self):
        old_img = Profile.objects.filter(pk=self.pk).first().image.path
        super().save()

        new_img = self.image.path

        print('====================================')
        print(f'OLD IMG: {old_img}')
        print(f'NEW IMG: {new_img}')
        img = Image.open(new_img)

        if old_img != new_img:
            # image operation should catch the IOError if file cannot be written
            scale = max(256 / img.width, 256 / img.height)
            img = img.resize((round(img.width * scale), round(img.height * scale)))
            img = img.crop((0, 0, 256, 256))
            img.save(new_img)

        try:
            if old_img != new_img and os.path.isfile(old_img):
                os.remove(old_img)
        except:
            pass
