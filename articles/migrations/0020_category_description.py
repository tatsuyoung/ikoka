# Generated by Django 2.2.10 on 2020-04-17 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_auto_20200414_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
