# Generated by Django 5.1.2 on 2024-11-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_app', '0003_generationprocess_server_int'),
    ]

    operations = [
        migrations.AddField(
            model_name='generationprocess',
            name='prompt',
            field=models.TextField(blank=True, help_text='user prompt', null=True),
        ),
    ]
