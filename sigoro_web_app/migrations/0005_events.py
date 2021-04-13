# Generated by Django 3.1.6 on 2021-03-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigoro_web_app', '0004_auto_20210318_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True, auto_now=True)),
                ('location', models.CharField(max_length=20)),
                ('headline', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='events_images')),
            ],
        ),
    ]