# Generated by Django 4.2 on 2023-04-15 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='fec_cmt',
            new_name='fec_like',
        ),
    ]