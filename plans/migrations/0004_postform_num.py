# Generated by Django 2.2.4 on 2019-08-14 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0003_preform_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='postform',
            name='num',
            field=models.CharField(default=8056069734, max_length=10),
            preserve_default=False,
        ),
    ]