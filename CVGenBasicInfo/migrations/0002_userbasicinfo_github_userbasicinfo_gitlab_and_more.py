# Generated by Django 4.0.4 on 2022-04-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVGenBasicInfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbasicinfo',
            name='github',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='userbasicinfo',
            name='gitlab',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='userbasicinfo',
            name='instagram',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='userbasicinfo',
            name='stackoverflow',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='userbasicinfo',
            name='telegram',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='userbasicinfo',
            name='whatsapp',
            field=models.CharField(default='', max_length=400),
        ),
    ]
