# Generated by Django 3.1.6 on 2021-02-09 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20210209_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='documento',
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
    ]
