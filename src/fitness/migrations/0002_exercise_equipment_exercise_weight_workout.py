# Generated by Django 5.0.6 on 2024-06-12 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='equipment',
            field=models.CharField(choices=[('B', 'Barbell'), ('BW', 'Bodyweight'), ('D', 'Dumbell'), ('R', 'Ropes')], default='BW', max_length=2),
        ),
        migrations.AddField(
            model_name='exercise',
            name='weight',
            field=models.JSONField(default=list),
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('focus', models.CharField(choices=[('A', 'Arms'), ('B', 'Back'), ('C', 'Chest'), ('F', 'Full Body'), ('L', 'Legs'), ('S', 'Shoulders')], default='F', max_length=1)),
                ('exercises', models.ManyToManyField(related_name='workout_exercises', to='fitness.exercise')),
            ],
        ),
    ]
