# Generated by Django 3.2 on 2021-04-13 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workeruser',
            name='phone_number',
            field=models.CharField(default=1231231231, max_length=13),
            preserve_default=False,
        ),
    ]