# Generated by Django 2.1.5 on 2019-02-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_complaint_seen_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='slug',
            field=models.SlugField(default=1, max_length=250),
        ),
    ]