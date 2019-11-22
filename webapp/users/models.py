from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')

    def __str__(self):
        return f'{self.user.username} Profile'


    # the following code uses magic numbers and harcoded literal strings: bad
    def save(self):
        old_img = Profile.objects.filter(pk=self.pk).first()
        if old_img is None:
            old_img = ''
        else:
            old_img = old_img.image.path

        super().save()

        new_img = self.image.path
        img = Image.open(new_img)

        if old_img != new_img:
            # image operation should catch the IOError if file cannot be written
            scale = max(256 / img.width, 256 / img.height)
            img = img.resize((round(img.width * scale), round(img.height * scale)))
            img = img.crop((0, 0, 256, 256))
            img.save(new_img)

        try:
            if old_img != new_img and os.path.isfile(old_img) and old_img != 'C:\\mushroom\\webapp\\media\\profile-default.jpg':
                os.remove(old_img)
        except:
            pass
