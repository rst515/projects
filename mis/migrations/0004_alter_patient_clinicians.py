# Generated by Django 4.0.5 on 2022-06-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0003_alter_appointment_clinician_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='clinicians',
            field=models.ManyToManyField(related_name='related_clinicians', to='mis.clinician'),
        ),
    ]
