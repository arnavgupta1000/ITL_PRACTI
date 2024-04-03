# Generated by Django 4.2.11 on 2024-04-02 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0006_alter_subject_staff'),
        ('students', '0002_auto_20201124_0614'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSubjectAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corecode.subject')),
            ],
        ),
    ]