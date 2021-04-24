# Generated by Django 2.2.4 on 2019-11-21 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_book_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('Plane_ID', models.CharField(max_length=50)),
                ('F', models.CharField(max_length=50)),
                ('T', models.CharField(max_length=50)),
                ('departing', models.DateField()),
                ('returning', models.DateField()),
                ('adults', models.IntegerField()),
                ('children', models.IntegerField()),
                ('Departure_Time', models.CharField(max_length=50)),
                ('Arrival_Time', models.CharField(max_length=50)),
                ('Departure_City', models.CharField(max_length=50)),
                ('Arrival_City', models.CharField(max_length=50)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]