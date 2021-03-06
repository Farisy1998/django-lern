# Generated by Django 4.0.2 on 2022-03-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=15)),
                ('course', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=20)),
                ('start_time', models.TimeField(max_length=20)),
                ('end_time', models.TimeField(max_length=20)),
                ('qp', models.FileField(upload_to='')),
            ],
        ),
    ]
