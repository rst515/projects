# Generated by Django 4.0.5 on 2022-06-22 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mis', '0008_clinician_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='is_prescription',
            field=models.BooleanField(default=False),
        ),
    ]
