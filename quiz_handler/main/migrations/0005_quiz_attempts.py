# Generated by Django 4.1.2 on 2022-10-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_quiz_author_alter_quiz_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='attempts',
            field=models.JSONField(blank=True, default={}),
        ),
    ]
