# Generated by Django 4.2.11 on 2024-04-03 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_studentsubjectassignment_unique_together'),
        ('corecode', '0007_delete_academicsession_delete_academicterm'),
        ('result', '0008_alter_studentassignment_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='studentassignment',
            unique_together={('student', 'subject')},
        ),
    ]
