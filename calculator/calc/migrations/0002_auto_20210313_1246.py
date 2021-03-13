# Generated by Django 3.1.4 on 2021-03-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='storage',
            options={'verbose_name': 'storage', 'verbose_name_plural': 'storages'},
        ),
        migrations.AlterModelOptions(
            name='truck',
            options={'verbose_name': 'truck', 'verbose_name_plural': 'trucks'},
        ),
        migrations.AddField(
            model_name='truck',
            name='max_carrying_capacity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='truck',
            name='model',
            field=models.CharField(db_index=True, default=0, max_length=200),
            preserve_default=False,
        ),
    ]
