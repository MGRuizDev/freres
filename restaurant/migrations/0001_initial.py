# Generated by Django 2.1.4 on 2019-04-08 07:03

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(choices=[('Alamo', 'Alamo'), ('Capistrano', 'Capistrano'), ('San Jose', 'San Jose'), ('Espada', 'Espada'), ('Terrace', 'Terrace')], max_length=15)),
                ('reservation_date', models.DateField()),
                ('purpose', models.TextField(max_length=1000)),
                ('additional_services', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('food', 'food'), ('flowers', 'flowers'), ('candels', 'candels'), ('valet perking', 'valet parking')], max_length=34, null=True)),
                ('special_request', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=50)),
                ('booking_info', models.OneToOneField(blank=True, null=True, on_delete='CASCADE', to='restaurant.BookingInformation')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(choices=[('debit', 'debit'), ('credit', 'credit')], max_length=6)),
                ('name_on_card', models.CharField(max_length=30)),
                ('card_number', models.CharField(max_length=20)),
                ('expiration_date', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='payment_info',
            field=models.OneToOneField(blank=True, null=True, on_delete='CASCADE', to='restaurant.PaymentInformation'),
        ),
    ]
