# Generated by Django 4.2.5 on 2024-01-22 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Olsi_App', '0002_product_db_prdt_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_db',
            name='PRDT_Benefits',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product_db',
            name='PRDT_Description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product_db',
            name='PRDT_Features',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product_db',
            name='PRDT_Usage',
            field=models.TextField(null=True),
        ),
    ]
