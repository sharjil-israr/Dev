# Generated by Django 3.2.10 on 2022-01-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_engine', '0009_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='section',
            field=models.CharField(choices=[('-1', 'others'), ('0', 'profile'), ('1', 'setting'), ('2', 'driver'), ('3', 'vehicle'), ('4', 'journey'), ('5', 'hsse'), ('6', 'reports')], default='0', max_length=10),
        ),
    ]
