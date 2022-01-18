# Generated by Django 3.2.7 on 2022-01-18 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_alter_application_hardware_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='hardware_preference',
            field=models.CharField(blank=True, help_text='Please indicate your preference for using hardware in this hackathon (optional)', max_length=10, null=True),
        ),
    ]
