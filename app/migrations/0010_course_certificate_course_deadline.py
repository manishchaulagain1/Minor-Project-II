# Generated by Django 4.0.4 on 2022-07-23 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_language_course_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Certificate',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='Deadline',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
