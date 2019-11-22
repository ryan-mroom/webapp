from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
import os


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    source = models.CharField(max_length=64)
    link_url = models.CharField(max_length=128)
    link_title = models.CharField(max_length=128)
    tags = models.CharField(max_length=128)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='newsfeed-default.png', upload_to='newsfeed_pics/')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newsfeed-post-detail', kwargs={'pk': self.pk})

    # the following code uses magic numbers and harcoded literal strings: bad
    def save(self):
        old_img = Post.objects.filter(pk=self.pk).first()
        print(type(old_img))
        if old_img is None:
            old_img = ''
        else:
            old_img = old_img.image.path

        super().save()

        new_img = self.image.path
        img = Image.open(new_img)

        if old_img != new_img:
            # image operation should catch the IOError if file cannot be written
            scale = max(568 / img.width, 196 / img.height)
            img = img.resize((round(img.width * scale), round(img.height * scale)))
            img = img.crop((0, 0, 568, 196))
            img.save(new_img)

        try:
            if old_img != new_img and os.path.isfile(old_img) and old_img != 'C:\\mushroom\\webapp\\media\\newsfeed-default.jpg':
                os.remove(old_img)
        except:
            pass