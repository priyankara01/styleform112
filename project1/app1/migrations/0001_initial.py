# Generated by Django 4.1.3 on 2022-12-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=89)),
                ('address', models.CharField(max_length=88)),
                ('mail', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
