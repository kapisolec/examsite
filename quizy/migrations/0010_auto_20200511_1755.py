# Generated by Django 3.0.6 on 2020-05-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizy', '0009_auto_20200511_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wyborodpowiedzi',
            name='Odpowiedz',
            field=models.CharField(max_length=50, null=True),
        ),
    ]