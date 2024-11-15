# Generated by Django 5.1.3 on 2024-11-15 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_cat_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cat',
            name='description',
            field=models.TextField(max_length=250),
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Feeeding Date')),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.cat')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
