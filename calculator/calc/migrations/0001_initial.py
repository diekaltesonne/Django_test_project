# Generated by Django 3.1.4 on 2021-03-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percentage_SiO2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percentage_Fe', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'storage',
                'verbose_name_plural': 'storages',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('carrying_capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percentage_SiO2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percentage_Fe', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'truck',
                'verbose_name_plural': 'trucks',
                'ordering': ('name',),
            },
        ),
    ]
