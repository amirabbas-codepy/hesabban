# Generated by Django 5.1.2 on 2024-10-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_TRC', '0002_trancion_code_trancion_date_trancion_descripition_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trancion',
            name='pain',
        ),
        migrations.AddField(
            model_name='trancion',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='trancion',
            name='status_TRC',
            field=models.CharField(choices=[('incom', 'incom'), ('cost', 'cost')], max_length=5, null=True),
        ),
    ]