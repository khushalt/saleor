# Generated by Django 3.0.6 on 2020-06-22 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0084_auto_20200522_0522"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Invoice",
        ),
    ]
