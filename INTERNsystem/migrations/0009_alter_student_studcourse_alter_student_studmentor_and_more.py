# Generated by Django 4.1.7 on 2023-10-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INTERNsystem', '0008_alter_internship_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='StudCourse',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='StudMentor',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='student',
            name='StudName',
            field=models.CharField(max_length=70),
        ),
    ]