# Generated by Django 4.2.4 on 2023-08-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_visibilty_palette_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='palette_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='username',
            field=models.CharField(max_length=50),
        ),
    ]
