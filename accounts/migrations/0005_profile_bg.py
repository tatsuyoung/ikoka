# Generated by Django 2.2.13 on 2020-07-02 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bg',
            field=models.ImageField(blank=True, help_text='著作権を確認してください。', null=True, upload_to=''),
        ),
    ]