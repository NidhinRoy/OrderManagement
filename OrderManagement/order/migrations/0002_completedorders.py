# Generated by Django 5.1.1 on 2024-09-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('model_no', models.CharField(max_length=255)),
                ('copy', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('franchise_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
