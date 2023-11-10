# Generated by Django 3.2.18 on 2023-04-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0011_alter_basicaddon_service_fee_flat_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
                ('rate', models.IntegerField(default=5, help_text='Numbers added here are in percentage (5 = 5%)')),
                ('active', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Tax Rates',
            },
        ),
    ]