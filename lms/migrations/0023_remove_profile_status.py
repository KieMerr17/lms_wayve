# Generated by Django 4.2.16 on 2024-10-28 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0022_profile_assigned_qa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='status',
        ),
    ]
