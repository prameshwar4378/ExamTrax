# Generated by Django 4.2 on 2023-07-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0018_alter_customuser_student_prn_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='is_result_declared',
            field=models.BooleanField(default=False),
        ),
    ]
