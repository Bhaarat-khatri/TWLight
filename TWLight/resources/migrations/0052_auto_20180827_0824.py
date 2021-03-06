# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-27 08:24


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("resources", "0051_auto_20180815_1132")]

    operations = [
        migrations.AddField(
            model_name="partner",
            name="accounts_available",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Add number of new accounts to the existing value, not by reseting it to zero.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="stream",
            name="accounts_available",
            field=models.PositiveSmallIntegerField(
                blank=True,
                help_text="Add number of new accounts to the existing value, not by reseting it to zero.",
                null=True,
            ),
        ),
    ]
