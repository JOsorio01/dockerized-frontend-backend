# Generated by Django 3.2.2 on 2021-05-10 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.area')),
            ],
        ),
    ]
