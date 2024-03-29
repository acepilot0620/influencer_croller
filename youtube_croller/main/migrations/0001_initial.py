# Generated by Django 3.0.1 on 2020-02-06 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celly_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_checked', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Instagram_result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_id', models.CharField(max_length=50)),
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
        migrations.CreateModel(
            name='Youtube_result',
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
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insta_id', models.CharField(max_length=30)),
                ('influencer', models.CharField(max_length=30)),
                ('feed_condition', models.CharField(max_length=30)),
                ('is_confirmed', models.BooleanField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Contract')),
            ],
        ),
    ]
