# Generated by Django 3.0.6 on 2020-05-11 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizy', '0006_auto_20200511_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pytania',
            name='tworca',
            field=models.ForeignKey(default='kacper', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
