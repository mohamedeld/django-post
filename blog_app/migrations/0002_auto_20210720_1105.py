# Generated by Django 3.2.5 on 2021-07-20 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(default='test1@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
