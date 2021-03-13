# Generated by Django 3.0.7 on 2020-08-08 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserAuth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Settings', serialize=False, to='UserAuth.User')),
                ('dark_color_value', models.CharField(blank=True, default='Black', max_length=500, null=True)),
                ('change_dark_color', models.BooleanField(default=False)),
                ('light_color_value', models.CharField(blank=True, default='White', max_length=500, null=True)),
                ('change_light_color', models.BooleanField(default=False)),
                ('voice_assistant', models.BooleanField(default=True)),
                ('use_numpad_keys_for_movement', models.BooleanField(default=True, verbose_name='use numpad keys for movement of pieces')),
                ('keys_for_mevement', models.CharField(blank=True, default='numpad', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Settings',
            },
        ),
    ]