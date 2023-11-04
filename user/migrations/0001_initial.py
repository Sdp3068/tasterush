# Generated by Django 4.2.6 on 2023-10-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('mobile_no', models.BigIntegerField(unique=True)),
            ],
            options={
                'db_table': 'user_table',
                'managed': False,
            },
        ),
    ]