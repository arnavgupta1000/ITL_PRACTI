# Generated by Django 4.2.11 on 2024-03-31 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0003_staff_empid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='empid',
        ),
        migrations.AddField(
            model_name='staff',
            name='EmpId',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
