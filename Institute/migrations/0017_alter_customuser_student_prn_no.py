# Generated by Django 4.2 on 2023-07-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Institute', '0016_rename_exam_time_exam_exam_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='student_prn_no',
            field=models.BigIntegerField(null=True),
        ),
    ]
