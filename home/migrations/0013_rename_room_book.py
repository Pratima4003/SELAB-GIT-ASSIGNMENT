# Generated by Django 4.2 on 2023-05-18 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_room_options_remove_room_book_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='Book',
        ),
    ]
