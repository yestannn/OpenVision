# Generated by Django 4.0.3 on 2022-05-05 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_alter_teammembers_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='team.team'),
        ),
    ]
