# Generated by Django 4.2.1 on 2023-05-21 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_librarian_student_alter_room_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarian',
            name='requested_books',
            field=models.ManyToManyField(blank=True, to='home.room'),
        ),
    ]
