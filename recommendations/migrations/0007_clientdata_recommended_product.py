# Generated by Django 5.1.1 on 2024-11-06 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0006_alter_clientdata_client_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientdata',
            name='recommended_product',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
