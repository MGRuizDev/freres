# Generated by Django 2.1 on 2018-09-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_bookinginformation_additional_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinginformation',
            name='room',
            field=models.CharField(choices=[('Alamo', 'Alamo'), ('Capistrano', 'Capistrano'), ('San Jose', 'San Jose'), ('Espada', 'Espada'), ('Terrace', 'Terrace')], max_length=15),
        ),
        migrations.AlterField(
            model_name='guest',
            name='booking_info',
            field=models.OneToOneField(blank=True, null=True, on_delete='CASCADE', to='restaurant.BookingInformation'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='guest',
            name='payment_info',
            field=models.OneToOneField(blank=True, null=True, on_delete='CASCADE', to='restaurant.PaymentInformation'),
        ),
        migrations.AlterField(
            model_name='paymentinformation',
            name='name_on_card',
            field=models.CharField(max_length=30),
        ),
    ]
