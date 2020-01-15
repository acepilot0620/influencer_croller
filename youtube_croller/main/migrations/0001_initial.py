# Generated by Django 2.2.7 on 2020-01-09 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=100)),
                ('subscriber_num', models.FloatField()),
                ('not_int_subscriber_num', models.CharField(max_length=100)),
                ('ten_avg_visit_num', models.CharField(max_length=100)),
                ('profile_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=20)),
            ],
        ),
    ]