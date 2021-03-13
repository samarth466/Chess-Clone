# Generated by Django 3.1.3 on 2020-12-27 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
        ('UserAuth', '0003_auto_20200822_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='game.game'),
        ),
    ]
