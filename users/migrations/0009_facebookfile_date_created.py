# Generated by Django 2.2.2 on 2019-09-26 11:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190925_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='facebookfile',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]