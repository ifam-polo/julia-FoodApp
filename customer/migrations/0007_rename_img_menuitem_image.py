# Generated by Django 3.2 on 2023-03-14 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_rename_descricao_menuitem_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='img',
            new_name='image',
        ),
    ]