# Generated by Django 4.2.11 on 2024-04-03 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0007_delete_academicsession_delete_academicterm'),
        ('students', '0004_alter_studentsubjectassignment_unique_together'),
        ('result', '0006_alter_studentassignment_options_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentassignment',
            unique_together={('student', 'subject', 'grade')},
        ),
    ]
