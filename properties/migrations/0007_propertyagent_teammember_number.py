# Generated by Django 4.2.7 on 2024-06-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_rename_calltoaction_propertyagent_calltoaction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyagent_teammember',
            name='number',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]