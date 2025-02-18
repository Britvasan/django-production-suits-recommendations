# Generated by Django 5.1.1 on 2024-10-25 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0002_alter_clientdata_pickup_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdata',
            name='client_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='customization',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='pickup_date',
            field=models.DateField(null=True),
        ),
    ]
