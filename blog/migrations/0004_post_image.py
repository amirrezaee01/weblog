# Generated by Django 4.2.13 on 2024-08-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/default.jpg', upload_to='blog/'),
        ),
    ]
