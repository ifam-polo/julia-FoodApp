# Generated by Django 3.2 on 2023-03-14 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_rename_name_category_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='nome',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='menuitem',
            old_name='nome',
            new_name='name',
        ),
    ]
