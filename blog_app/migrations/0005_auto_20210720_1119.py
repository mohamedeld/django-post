# Generated by Django 3.2.5 on 2021-07-20 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_auto_20210720_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('WB', 'web Developement'), ('DB', 'Desktop Developement'), ('DS', 'Data Science')], max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
