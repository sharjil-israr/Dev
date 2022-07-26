# Generated by Django 4.0 on 2022-01-03 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_engine', '0006_rename_role_groupwisepermission_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='section',
            field=models.CharField(choices=[('0', 'profile'), ('1', 'setting'), ('2', 'driver'), ('3', 'vehicle'), ('4', 'journey'), ('5', 'hsse'), ('6', 'reports')], default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts_engine.customuser'),
        ),
    ]
