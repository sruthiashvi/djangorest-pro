# Generated by Django 2.2.4 on 2019-08-13 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0006_dongleplans'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('femail', models.IntegerField()),
                ('fmessage', models.CharField(max_length=1000)),
            ],
        ),
    ]
