# Generated by Django 3.2.10 on 2022-02-05 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_engine', '0011_auto_20220205_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverrecruitment',
            name='company_induction_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/company_induction/'),
        ),
        migrations.AddField(
            model_name='driverrecruitment',
            name='fire_fighting_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/fire_fighting/'),
        ),
        migrations.AddField(
            model_name='driverrecruitment',
            name='first_aid_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/first_aid/'),
        ),
        migrations.AddField(
            model_name='driverrecruitment',
            name='medical_test_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/medical/'),
        ),
        migrations.AlterField(
            model_name='driverrecruitment',
            name='shell_induction_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/shell_induction/'),
        ),
    ]
