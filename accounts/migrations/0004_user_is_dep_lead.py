# Generated by Django 5.0.3 on 2024-03-28 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_dep_lead',
            field=models.BooleanField(default=False),
        ),
    ]
