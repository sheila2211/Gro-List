# Generated by Django 5.1.4 on 2025-01-02 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_post_post_type_alter_post_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='neccessity',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
