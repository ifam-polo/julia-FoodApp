# Generated by Django 3.2 on 2023-03-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_auto_20230314_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
