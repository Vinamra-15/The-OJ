# Generated by Django 4.0.5 on 2022-06-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('difficulty', models.IntegerField(choices=[(0, 'EASY'), (1, 'MEDIUM'), (2, 'HARD')], default=0)),
                ('input', models.TextField(default='', help_text='Input format')),
                ('output', models.TextField(default='', help_text='Expected output format')),
                ('time_limit', models.IntegerField(default=1000, help_text='in milliseconds')),
            ],
        ),
    ]
