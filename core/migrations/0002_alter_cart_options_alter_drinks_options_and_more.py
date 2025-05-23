# Generated by Django 5.2.1 on 2025-05-20 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name_plural': 'Cart'},
        ),
        migrations.AlterModelOptions(
            name='drinks',
            options={'verbose_name': 'Drinks', 'verbose_name_plural': 'Drinks'},
        ),
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name_plural': 'Food'},
        ),
        migrations.RemoveField(
            model_name='cart',
            name='is_paid',
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='drinks',
            name='size',
            field=models.CharField(choices=[('s', 'Short'), ('t', 'Tall'), ('g', 'Grande'), ('v', 'Venti')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
