# Generated by Django 5.1.1 on 2024-09-20 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0002_alter_employee_hire_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('established_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='hrms.company'),
        ),
    ]
