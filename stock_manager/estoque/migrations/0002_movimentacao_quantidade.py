# Generated by Django 5.1.4 on 2024-12-07 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacao',
            name='quantidade',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
