# Generated by Django 4.0.3 on 2023-12-20 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0025_referer_click_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
