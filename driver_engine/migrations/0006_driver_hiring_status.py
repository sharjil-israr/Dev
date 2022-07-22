# Generated by Django 3.2.10 on 2022-01-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_engine', '0005_driverbehaviourtest'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='hiring_status',
            field=models.CharField(choices=[('0', 'In Active'), ('1', 'Active'), ('2', 'On Leave')], default='0', max_length=10),
        ),
    ]