# Generated by Django 2.0.2 on 2018-02-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('college_code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
    ]
