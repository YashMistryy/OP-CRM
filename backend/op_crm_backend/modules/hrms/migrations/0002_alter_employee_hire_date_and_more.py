# Generated by Django 5.1.1 on 2024-09-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(blank=True, max_length=50, null=True, verbose_name='hiring date'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='immediate_manager',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='immediate manager of employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_role',
            field=models.CharField(choices=[('intern', 'Intern'), ('employee', 'Employee'), ('lead', 'Lead'), ('manager', 'Manager'), ('chief_officer', 'Chief Officer')], max_length=50, verbose_name='current job role'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='pancard_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='identification number for eg. pancard no.'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='reason_for_resign',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='reason for resignation'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='working_status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('on_leave', 'On Leave'), ('on_notice_period', 'On Notice Period'), ('terminated', 'Terminated')], max_length=50, null=True, verbose_name='working status'),
        ),
    ]
