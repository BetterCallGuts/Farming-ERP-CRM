# Generated by Django 4.2.4 on 2023-08-18 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_group_warehouse_cow_food_cow_is_male_cow_logs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.foodcategory'),
        ),
    ]
