# Generated by Django 3.1.6 on 2021-03-17 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='notices')),
                ('description', models.CharField(max_length=50)),
                ('size', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
    ]
