# Generated by Django 4.0.5 on 2022-07-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='compiler',
            field=models.CharField(choices=[('0', 'python')], default='python', max_length=30),
        ),
    ]
