# Generated by Django 4.2.16 on 2024-10-28 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0020_remove_profile_team_members_profile_assigned_qa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='assigned_qa',
        ),
    ]
