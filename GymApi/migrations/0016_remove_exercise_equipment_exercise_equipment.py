# Generated by Django 4.0.5 on 2023-04-02 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GymApi', '0015_training_remove_session_trainday_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='equipment',
        ),
        migrations.AddField(
            model_name='exercise',
            name='equipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GymApi.equipment'),
        ),
    ]
