# Generated by Django 3.0.6 on 2020-05-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizy', '0016_auto_20200511_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzytkownicy',
            name='haslo',
            field=models.CharField(default=123, max_length=30),
            preserve_default=False,
        ),
    ]
