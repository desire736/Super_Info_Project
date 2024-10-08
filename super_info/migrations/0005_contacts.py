# Generated by Django 5.0.8 on 2024-08-12 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_info', '0004_category_publications_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
