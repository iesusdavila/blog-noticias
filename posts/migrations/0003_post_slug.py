# Generated by Django 4.2 on 2023-04-15 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_fec_cmt_like_fec_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='arreglame'),
            preserve_default=False,
        ),
    ]