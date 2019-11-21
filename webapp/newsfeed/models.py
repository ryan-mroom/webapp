from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from math import ceil
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
    image = models.ImageField(default='newsfeed-default.jpg', upload_to='newsfeed_pics/')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('newsfeed-post-detail', kwargs={'pk':self.pk})


    def save(self):
        try:
            current_img = Post.objects.filter(pk=self.pk).first().image.path
            if current_img != self.image.path:
                os.remove(current_img)
        except:
            pass

        super().save()

        img = Image.open(self.image.path)

        # the following code uses magic numbers: bad
        scale = max(568/img.width, 196/img.height)
        img_size = (ceil(img.width * scale), ceil(img.height * scale))
        img.thumbnail(img_size)
        img = img.crop((0, 0, 568, 196))

        img.save(self.image.path)