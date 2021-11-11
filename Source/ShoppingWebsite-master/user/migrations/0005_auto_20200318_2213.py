# Generated by Django 3.0.4 on 2020-03-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_myuser_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='sex',
            field=models.IntegerField(choices=[(0, 'Không xác định'), (-1, 'Nữ'), (1, 'Nam')], default=0),
        ),
    ]
