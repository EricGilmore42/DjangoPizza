# Generated by Django 3.0.5 on 2022-11-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizzas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_names', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Topings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]