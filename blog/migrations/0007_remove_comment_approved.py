# Generated by Django 4.2.13 on 2024-08-27 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_tag_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved',
        ),
    ]
