# Generated by Django 4.1.7 on 2023-04-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(default='test1'),
            preserve_default=False,
        ),
    ]
