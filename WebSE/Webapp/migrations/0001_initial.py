# Generated by Django 3.1.2 on 2020-10-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDonationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_fd', models.CharField(max_length=256)),
                ('phone_fd', models.IntegerField()),
                ('Location_fd', models.TextField()),
                ('Amount_fd', models.IntegerField()),
                ('FoodType_fd', models.CharField(max_length=256)),
                ('Reason_fd', models.CharField(max_length=256)),
            ],
        ),
    ]
