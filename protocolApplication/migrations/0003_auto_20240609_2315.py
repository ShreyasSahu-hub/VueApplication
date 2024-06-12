# Generated by Django 3.2.25 on 2024-06-09 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protocolApplication', '0002_auto_20240608_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caloriedetail',
            name='owner',
            field=models.ForeignKey(blank=True, default=1717971330, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='taskdetail',
            name='amountOfTime',
            field=models.DurationField(),
        ),
        migrations.AlterField(
            model_name='taskdetail',
            name='owner',
            field=models.ForeignKey(blank=True, default=1717971330, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]