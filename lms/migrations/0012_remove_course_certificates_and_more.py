# Generated by Django 4.2.4 on 2024-09-28 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0011_course_enrolled_users_profile_certificate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='certificates',
        ),
        migrations.RemoveField(
            model_name='course',
            name='enrolled_users',
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
