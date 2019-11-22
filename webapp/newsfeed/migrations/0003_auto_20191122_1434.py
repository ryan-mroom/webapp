# Generated by Django 2.2.7 on 2019-11-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='newsfeed-default.png', upload_to='newsfeed_pics/'),
        ),
    ]
