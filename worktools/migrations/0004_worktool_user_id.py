# Generated by Django 3.1.7 on 2021-06-06 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('worktools', '0003_auto_20210521_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktool',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tools', to=settings.AUTH_USER_MODEL),
        ),
    ]
