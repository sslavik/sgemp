# Generated by Django 2.2.3 on 2019-10-27 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomProveedor', models.TextField()),
                ('direccion', models.TextField()),
                ('nif', models.CharField(max_length=9)),
                ('telefono', models.TextField()),
                ('telefono2', models.TextField()),
                ('email', models.TextField()),
                ('web', models.TextField()),
            ],
        ),
    ]