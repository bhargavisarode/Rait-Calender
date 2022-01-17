# Generated by Django 3.2.6 on 2021-09-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20210906_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='EXTCEvent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('CS', 'CS'), ('IT', 'IT'), ('EXTC', 'EXTC'), ('INSTRU', 'INSTRU')], max_length=100)),
                ('time', models.DateTimeField()),
                ('desc', models.CharField(max_length=10000000000000)),
            ],
            options={
                'db_table': 'EXTCEvent',
            },
        ),
        migrations.CreateModel(
            name='INSTRUEvent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('CS', 'CS'), ('IT', 'IT'), ('EXTC', 'EXTC'), ('INSTRU', 'INSTRU')], max_length=100)),
                ('time', models.DateTimeField()),
                ('desc', models.CharField(max_length=10000000000000)),
            ],
            options={
                'db_table': 'INSTRUEvent',
            },
        ),
        migrations.CreateModel(
            name='ITEvent',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('CS', 'CS'), ('IT', 'IT'), ('EXTC', 'EXTC'), ('INSTRU', 'INSTRU')], max_length=100)),
                ('time', models.DateTimeField()),
                ('desc', models.CharField(max_length=10000000000000)),
            ],
            options={
                'db_table': 'ITEvent',
            },
        ),
    ]