# Generated by Django 3.2.25 on 2024-06-09 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocolApplication', '0003_auto_20240609_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caloriedetail',
            name='owner',
            field=models.ForeignKey(blank=True, default=1717971665, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='taskdetail',
            name='owner',
            field=models.ForeignKey(blank=True, default=1717971665, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
