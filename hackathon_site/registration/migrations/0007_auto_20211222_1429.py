# Generated by Django 3.2.7 on 2021-12-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0006_auto_20211222_1315"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="address1",
            field=models.CharField(
                blank=True, help_text="e.g. 35 St George St", max_length=255, null=True
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="address2",
            field=models.CharField(
                blank=True, help_text="e.g. Apt. No. 13", max_length=255, null=True
            ),
        ),
    ]