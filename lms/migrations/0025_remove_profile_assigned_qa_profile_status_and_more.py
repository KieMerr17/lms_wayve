# Generated by Django 4.2.16 on 2024-10-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0024_alter_profile_role_investigation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='assigned_qa',
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('On-road Testing', 'On-road Testing'), ('Refresher required', 'Refresher required'), ('Off road', 'Off road')], default='On§-road Testing', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('VSO', 'VSO'), ('Trainer', 'Trainer'), ('QA', 'QA'), ('Admin', 'Admin')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Investigation',
        ),
    ]
