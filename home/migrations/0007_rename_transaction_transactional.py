# Generated by Django 4.2.16 on 2024-11-04 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_transaction_created_on'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transaction',
            new_name='Transactional',
        ),
    ]
