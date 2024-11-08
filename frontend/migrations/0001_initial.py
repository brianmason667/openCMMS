# Generated by Django 3.1.1 on 2024-11-04 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.IntegerField(unique=True)),
                ('part_number', models.CharField(blank=True, max_length=50)),
                ('alt_part_number', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(max_length=255)),
                ('bin_location', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.BooleanField(default=True)),
                ('manufacturer', models.CharField(max_length=100)),
                ('manufacturer_part_number', models.CharField(blank=True, max_length=50, null=True)),
                ('vpart_number', models.CharField(blank=True, max_length=50, null=True)),
                ('on_hand', models.IntegerField()),
                ('on_order', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('history', models.TextField(blank=True, null=True)),
                ('part_class', models.CharField(max_length=50)),
                ('last_order', models.DateField(blank=True, null=True)),
                ('lead_time', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('order_status', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('order_point', models.IntegerField(blank=True, null=True)),
                ('order_quantity', models.IntegerField(blank=True, null=True)),
                ('unit_of_measure', models.CharField(max_length=50)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='frontend.supplier')),
            ],
        ),
    ]
