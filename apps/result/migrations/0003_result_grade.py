# Generated by Django 4.2.11 on 2024-04-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0002_remove_result_session_remove_result_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='grade',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
