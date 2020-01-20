# Generated by Django 2.2.7 on 2020-01-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_features'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='features',
            options={'ordering': ['name'], 'verbose_name': 'Complemento', 'verbose_name_plural': 'Complementos'},
        ),
        migrations.AlterModelOptions(
            name='subservice',
            options={'ordering': ['name'], 'verbose_name': 'subServicio', 'verbose_name_plural': 'subServicios'},
        ),
        migrations.AddField(
            model_name='service',
            name='features',
            field=models.ManyToManyField(to='services.Features'),
        ),
    ]