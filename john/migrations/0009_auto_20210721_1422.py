# Generated by Django 3.1.7 on 2021-07-21 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0008_results_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
