# Generated by Django 3.1.7 on 2021-07-23 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0016_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
