# Generated by Django 3.0.8 on 2020-09-25 15:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200925_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='transaction_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
