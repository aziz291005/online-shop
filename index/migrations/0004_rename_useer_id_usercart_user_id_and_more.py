# Generated by Django 4.1 on 2022-08-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_usercart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercart',
            old_name='useer_id',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='usercart',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]