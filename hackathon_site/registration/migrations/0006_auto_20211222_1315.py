# Generated by Django 3.2.7 on 2021-12-22 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0005_auto_20211220_2142"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="address1",
            field=models.CharField(
                blank=True, help_text="35 St George St", max_length=255
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="address2",
            field=models.CharField(
                blank=True, help_text="Apt. No. 13", max_length=255, null=True
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="city",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="application",
            name="country",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="application",
            name="postal_code",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name="application",
            name="program",
            field=models.CharField(
                default="", help_text="Program or Major", max_length=255
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="application",
            name="hardware_preference",
            field=models.CharField(
                help_text="Please indicate your preference for using hardware in this hackathon",
                max_length=10,
            ),
        ),
    ]
