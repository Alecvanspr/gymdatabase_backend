# Generated by Django 4.0.5 on 2023-04-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymApi', '0016_remove_exercise_equipment_exercise_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='image',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='help_video',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
