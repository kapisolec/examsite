# Generated by Django 3.0.6 on 2020-05-13 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizy', '0018_auto_20200513_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wyniki',
            name='odpowiedz1',
        ),
        migrations.RemoveField(
            model_name='wyniki',
            name='odpowiedz2',
        ),
        migrations.RemoveField(
            model_name='wyniki',
            name='odpowiedz3',
        ),
        migrations.RemoveField(
            model_name='wyniki',
            name='uzytkownik',
        ),
        migrations.AlterField(
            model_name='wyborodpowiedzi',
            name='pytanie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quizy.Pytania'),
        ),
    ]
