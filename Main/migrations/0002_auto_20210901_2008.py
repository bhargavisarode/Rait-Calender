# Generated by Django 3.1.12 on 2021-09-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('CS', 'CS'), ('IT', 'IT'), ('EXTC', 'EXTC'), ('INSTRU', 'INSTRU')], max_length=100),
        ),
    ]