# Generated by Django 3.2.8 on 2021-11-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_alter_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(),
        ),
    ]
