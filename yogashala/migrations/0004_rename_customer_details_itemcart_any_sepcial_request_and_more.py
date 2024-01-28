# Generated by Django 4.2.6 on 2023-12-09 05:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("yogashala", "0003_remove_itemcart_email_remove_itemcart_completed_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="itemcart",
            old_name="customer_details",
            new_name="Any_sepcial_request",
        ),
        migrations.AddField(
            model_name="itemcart",
            name="Email",
            field=models.EmailField(default="anupthatal2@gmail.com", max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="itemcart",
            name="location",
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="itemcart",
            name="name",
            field=models.CharField(blank=True, null=True),
        ),
    ]