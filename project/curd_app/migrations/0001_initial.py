# Generated by Django 5.0.3 on 2024-03-21 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('car_company', models.CharField(max_length=20)),
                ('car_name_mode', models.CharField(choices=[('bolero', 'Bolero'), ('creta', 'Creta'), ('kia', 'Kia'), ('thar', 'Thar')], max_length=10)),
                ('car_model_mode', models.CharField(choices=[('old', 'Old'), ('new', 'New')], max_length=10)),
                ('car_capacity', models.CharField(max_length=20)),
                ('car_cc', models.CharField(max_length=20)),
            ],
        ),
    ]
