# Generated by Django 3.2.7 on 2021-12-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0009_auto_20211227_2342"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="city",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="application",
            name="postal_code",
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name="application",
            name="region",
            field=models.CharField(max_length=255),
        ),
    ]
