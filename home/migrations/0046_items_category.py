# Generated by Django 5.0.1 on 2024-11-07 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_alter_reviewrating_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.CharField(choices=[('Food', 'Food'), ('Drinks', 'Drinks')], default='Food', max_length=10),
        ),
    ]
