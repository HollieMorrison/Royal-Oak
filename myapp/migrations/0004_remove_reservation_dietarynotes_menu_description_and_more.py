# Generated by Django 5.1.2 on 2025-01-17 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_table_reservation_children_reservation_dietarynotes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='dietaryNotes',
        ),
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='dietary_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.table'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='children',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='party_size',
            field=models.PositiveIntegerField(),
        ),
    ]
