# Generated by Django 4.0.3 on 2022-04-03 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_usuario_alter_evento_data_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
