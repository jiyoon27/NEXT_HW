# Generated by Django 3.2 on 2021-04-15 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='movie', max_length=50),
            preserve_default=False,
        ),
    ]