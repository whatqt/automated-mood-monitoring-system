# Generated by Django 5.1.2 on 2025-03-10 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data_acceptance', '0002_alter_dataforanalysis_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponsesAI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('data_for_analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_acceptance.dataforanalysis')),
            ],
        ),
    ]
