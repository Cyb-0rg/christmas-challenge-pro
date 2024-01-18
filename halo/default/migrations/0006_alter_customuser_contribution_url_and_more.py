# Generated by Django 4.0.3 on 2023-11-22 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0005_rename_repo_link_customuser_expertise_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='contribution_url',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='issue_desc',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='project_impact',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='project_info',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='project_url',
            field=models.TextField(),
        ),
    ]
