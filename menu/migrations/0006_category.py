# Generated by Django 3.2 on 2021-12-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_menu_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_category', models.CharField(max_length=50)),
            ],
        ),
    ]