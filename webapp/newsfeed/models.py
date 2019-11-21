from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from math import ceil


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


    # NOTE: Need to delete old image before adding a new one.
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        # the following code uses magic numbers: bad
        scale_x = 568/img.width
        scale_y = 196/img.height
        if scale_x > scale_y:
            img_size = (ceil(img.width * scale_x), ceil(img.height * scale_x))
            img.thumbnail(img_size)
        elif scale_y > scale_x:
            img_size = (ceil(img.width * scale_y), ceil(img.height * scale_y))
            img.thumbnail(img_size)

        img = img.crop((0, 0, 568, 196))

        img.save(self.image.path)