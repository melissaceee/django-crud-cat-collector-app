# Generated by Django 5.1.3 on 2024-11-26 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_toy_cat_user_cat_toys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='color',
            field=models.CharField(default='#cccccc', max_length=20),
        ),
    ]