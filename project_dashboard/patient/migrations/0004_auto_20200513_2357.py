# Generated by Django 2.2 on 2020-05-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patientappointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientappointment',
            name='comment',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='patientappointment',
            name='treatmenttype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patienttreatment',
            name='parent_treatment',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
