# Generated by Django 2.2.3 on 2019-10-21 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(choices=[('A', 'Autonomo'), ('S', 'Sociedad'), ('P', 'Particular')], default='P', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCliente', models.TextField()),
                ('direccion', models.TextField()),
                ('nif', models.CharField(max_length=9)),
                ('telefono', models.TextField()),
                ('telefono2', models.TextField()),
                ('email', models.TextField()),
                ('web', models.TextField()),
                ('categoriaCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.CategoriaCliente')),
            ],
        ),
    ]
