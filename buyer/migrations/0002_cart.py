# Generated by Django 4.1.5 on 2023-02-16 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_products'),
        ('buyer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.products')),
            ],
        ),
    ]
