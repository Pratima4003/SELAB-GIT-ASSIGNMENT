# Generated by Django 4.2.1 on 2023-05-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_category_image_link_room_book_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='book_description',
            field=models.TextField(null=True),
        ),
    ]
