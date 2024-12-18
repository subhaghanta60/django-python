# Generated by Django 4.1.13 on 2024-12-16 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_restaurant_restaurant_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.DecimalField(decimal_places=2, max_digits=8)),
                ('datetime', models.DateTimeField()),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.restaurant')),
            ],
        ),
    ]