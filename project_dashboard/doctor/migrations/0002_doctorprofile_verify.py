# Generated by Django 2.2 on 2020-05-23 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='verify',
            field=models.BooleanField(null=True),
        ),
    ]
