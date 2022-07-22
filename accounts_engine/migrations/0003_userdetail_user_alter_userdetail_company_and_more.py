# Generated by Django 4.0 on 2022-01-01 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_engine', '0002_company_group_permission_role_userdetail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts_engine.customuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='accounts_engine.company'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='accounts_engine.group'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='accounts_engine.role'),
        ),
    ]