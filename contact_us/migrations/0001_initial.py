# Generated by Django 5.0.2 on 2024-02-09 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=14)),
                ('problem', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
