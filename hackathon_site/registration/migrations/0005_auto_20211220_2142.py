# Generated by Django 3.2.7 on 2021-12-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registration", "0004_application_rsvp"),
    ]

    operations = [
        migrations.RemoveField(model_name="application", name="data_agree",),
        migrations.RemoveField(model_name="application", name="q1",),
        migrations.RemoveField(model_name="application", name="q2",),
        migrations.RemoveField(model_name="application", name="q3",),
        migrations.AddField(
            model_name="application",
            name="email_agree",
            field=models.BooleanField(
                blank=True,
                default=True,
                help_text="I authorize MLH to send me pre- and post-event informational emails, which contain free credit and opportunities from their partners.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="hardware_preference",
            field=models.CharField(
                choices=[
                    (None, ""),
                    (
                        "pickup",
                        "I would like to pick up hardware in person at University of Toronto from the MakeUofT team.",
                    ),
                    (
                        "buy",
                        "I would like to buy my own hardware and would like to be reimbursed from the MakeUofT team (Note: reimbursement amount is TBD)",
                    ),
                ],
                default="pickup",
                help_text="Please indicate your preference for using hardware in this hackathon",
                max_length=100,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="how_many_hackathons",
            field=models.TextField(
                choices=[
                    (None, ""),
                    ("0", "0"),
                    ("1", "1"),
                    ("2", "2"),
                    ("3", "3"),
                    ("4", "4"),
                    ("5 or more", "5 or more"),
                ],
                default=0,
                help_text="How many hackathons have you been to?",
                max_length=100,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="logistics_agree",
            field=models.BooleanField(
                default=True,
                help_text='I authorize you to share my application/registration information with Major League Hackingfor event administration, ranking, and MLH administration in-line with the <a href="https://mlh.io/privacy">MLH Privacy Policy</a>. I further agree to the terms of both the <a href="https://github.com/MLH/mlh-policies/tree/master/prize-terms-and-conditions">MLH Contest Terms and Conditions</a> and the <a href="https://mlh.io/privacy">MLH Privacy Policy.</a>',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="referral_source",
            field=models.TextField(
                default="instagram",
                help_text="How did you hear about NewHacks?",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="region",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="application",
            name="resume_sharing",
            field=models.BooleanField(
                blank=True,
                default=True,
                help_text="I consent to IEEE UofT sharing my resume with event sponsors.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="tshirt_size",
            field=models.CharField(
                choices=[(None, ""), ("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL")],
                default="S",
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="what_hackathon_experience",
            field=models.TextField(
                default="",
                help_text="If you’ve been to a hackathon, briefly tell us your experience. If not, describe what you expect to see and experience.",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="what_technical_experience",
            field=models.TextField(
                default="",
                help_text="What is your technical experience with software and hardware?",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="application",
            name="why_participate",
            field=models.TextField(
                default="",
                help_text="Why do you want to participate in NewHacks?",
                max_length=1000,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="application",
            name="conduct_agree",
            field=models.BooleanField(
                help_text='I have read and agree to the <a href="https://static.mlh.io/docs/mlh-code-of-conduct.pdf">MLH code of conduct</a>.'
            ),
        ),
    ]
