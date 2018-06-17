# Generated by Django 2.0.3 on 2018-06-17 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('firstname', models.CharField(blank=True, default='', max_length=100)),
                ('lastname', models.CharField(blank=True, default='', max_length=100)),
                ('email', models.CharField(blank=True, default='', max_length=100)),
                ('password', models.CharField(blank=True, default='', max_length=50)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
