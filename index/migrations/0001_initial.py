# Generated by Django 4.1 on 2022-08-18 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.FloatField()),
                ('product_description', models.TextField()),
                ('product_count', models.IntegerField()),
                ('product_added_date', models.DateTimeField(auto_now_add=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.category')),
            ],
        ),
    ]
