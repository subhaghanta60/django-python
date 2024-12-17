# Generated by Django 4.1.13 on 2024-12-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='restaurant_type',
            field=models.CharField(choices=[('IN', 'Indian'), ('CH', 'Chinese'), ('IT', 'Italian'), ('GR', 'Greek'), ('MX', 'Mexican'), ('FF', 'Fast Food'), ('OT', 'other')], default='', max_length=2),
            preserve_default=False,
        ),
    ]
