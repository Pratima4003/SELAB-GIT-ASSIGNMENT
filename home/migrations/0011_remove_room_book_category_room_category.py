# Generated by Django 4.2 on 2023-05-18 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_room_options_room_book_issue_date_room_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='book_category',
        ),
        migrations.AddField(
            model_name='room',
            name='category',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='home.category'),
        ),
    ]
