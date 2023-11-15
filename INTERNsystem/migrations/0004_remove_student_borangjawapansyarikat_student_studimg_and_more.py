# Generated by Django 4.1.7 on 2023-10-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INTERNsystem', '0003_alter_internship_advid_alter_uploadbyadmin_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='BorangJawapanSyarikat',
        ),
        migrations.AddField(
            model_name='student',
            name='StudImg',
            field=models.ImageField(blank=True, null=True, upload_to='Student Profile Picture/'),
        ),
        migrations.AlterField(
            model_name='internship',
            name='EndDate',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='internship',
            name='Session',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='internship',
            name='StartDate',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
