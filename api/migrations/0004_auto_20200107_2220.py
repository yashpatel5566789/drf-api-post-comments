# Generated by Django 3.0.2 on 2020-01-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200107_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]