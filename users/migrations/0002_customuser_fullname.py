# Generated by Django 3.0.8 on 2020-07-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fullname',
            field=models.TextField(blank=True, null=''),
        ),
    ]