# Generated by Django 4.2.7 on 2024-06-27 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_propertyagent_teammember_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyagent_teammember',
            name='number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
