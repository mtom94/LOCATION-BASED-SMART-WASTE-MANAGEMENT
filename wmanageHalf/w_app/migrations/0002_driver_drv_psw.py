# Generated by Django 4.2.8 on 2024-02-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("w_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="driver",
            name="drv_psw",
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
