# Generated by Django 3.2 on 2021-04-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2App', '0002_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]