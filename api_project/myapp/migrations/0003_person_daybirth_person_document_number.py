# Generated by Django 4.2.9 on 2024-01-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_rename_name_person_first_name_person_age_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="daybirth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="person",
            name="document_number",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
