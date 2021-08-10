# Generated by Django 3.2.6 on 2021-08-10 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_remove_menuitem_schools_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='app_only',
            field=models.BooleanField(default=False, verbose_name='à la carte only'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('ENT', 'Entree'), ('SIDE', 'Side'), ('DEST', 'Dessert'), ('DRINK', 'Drink')], default='', max_length=6),
        ),
    ]
