# Generated by Django 4.2.7 on 2023-12-21 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jackets',
            name='photo',
            field=models.ImageField(default='a', upload_to='Jackets/'),
        ),
        migrations.AddField(
            model_name='jeans',
            name='photo',
            field=models.ImageField(default='a', upload_to='Jeans/'),
        ),
        migrations.AddField(
            model_name='shirts',
            name='photo',
            field=models.ImageField(default='a', upload_to='Shirts/'),
        ),
        migrations.AddField(
            model_name='t_shirts',
            name='photo',
            field=models.ImageField(default='a', upload_to='T-shirts'),
        ),
    ]