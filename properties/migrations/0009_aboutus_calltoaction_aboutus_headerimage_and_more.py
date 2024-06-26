# Generated by Django 4.2.7 on 2024-06-27 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_alter_propertyagent_teammember_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs_CallToAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cta_images')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs_HeaderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='header_images')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs_TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(upload_to='team_images')),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('twitter_url', models.URLField(blank=True, null=True)),
                ('instagram_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
