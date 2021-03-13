# Generated by Django 3.1.4 on 2021-03-13 19:17

from django.db import migrations, models
import django.db.models.deletion


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
                ('slug', models.SlugField(max_length=200, unique=True)),
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
                ('is_online', models.BooleanField(default=True)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('model', models.CharField(db_index=True, max_length=200)),
                ('carrying_capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_carrying_capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percentage_SiO2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percentage_Fe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Storage', to='calc.storage')),
            ],
            options={
                'verbose_name': 'truck',
                'verbose_name_plural': 'trucks',
                'ordering': ('name',),
            },
        ),
    ]
