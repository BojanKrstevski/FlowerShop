# Generated by Django 4.1.7 on 2023-06-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='type',
        ),
        migrations.AddField(
            model_name='article',
            name='occasion',
            field=models.CharField(blank=True, choices=[('1', 'birthday'), ('2', 'anniversary'), ('3', 'sympathy'), ('3', 'graduation'), ('3', 'getwell')], max_length=32, null=True),
        ),
    ]
