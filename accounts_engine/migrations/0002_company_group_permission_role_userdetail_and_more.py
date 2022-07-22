# Generated by Django 4.0 on 2021-12-30 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_engine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('0', 'developer'), ('1', 'setting'), ('2', 'driver'), ('3', 'vehicle'), ('4', 'journey'), ('4', 'hsse'), ('5', 'reports')], default='0', max_length=10)),
                ('url_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='accounts_engine.customuser')),
                ('custom_permission', models.ManyToManyField(related_name='custom_permissions', to='accounts_engine.Permission')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='accounts_engine.customuser')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='accounts_engine.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='RoleWisePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ManyToManyField(related_name='role_permissions', to='accounts_engine.Permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts_engine.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='GroupWisePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ManyToManyField(related_name='group_permissions', to='accounts_engine.Permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts_engine.customuser')),
            ],
        ),
    ]