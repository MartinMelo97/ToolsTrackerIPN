# Generated by Django 3.1.7 on 2021-04-16 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_workeruser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workeruser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
