# Generated by Django 3.2.5 on 2021-07-26 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_alter_analysis_cmd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='analysis.analysis'),
        ),
    ]
