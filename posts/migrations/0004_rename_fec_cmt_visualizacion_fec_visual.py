# Generated by Django 4.2 on 2023-04-16 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visualizacion',
            old_name='fec_cmt',
            new_name='fec_visual',
        ),
    ]
