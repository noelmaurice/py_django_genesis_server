# Generated by Django 3.2.4 on 2021-06-23 14:54

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Sample name', max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('filters', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(help_text='Filters', max_length=200), size=None)),
            ],
            options={
                'db_table': 'sample',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Part name', max_length=200)),
                ('value', models.CharField(help_text='Part value', max_length=200)),
                ('sample', models.ForeignKey(help_text='Sample', on_delete=django.db.models.deletion.CASCADE, to='sample.sample')),
            ],
            options={
                'db_table': 'part',
            },
        ),
    ]
