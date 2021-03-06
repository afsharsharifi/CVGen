# Generated by Django 4.0.4 on 2022-06-24 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVGenBasicInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbasicinfo',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='birthyear',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='firstname',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='github',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='gitlab',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='lastname',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='position',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='stackoverflow',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='telegram',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='template',
            field=models.CharField(blank=True, choices=[('1', 'Creative CV'), ('2', 'I???mRex'), ('3', 'Material CV'), ('4', 'Material Resume'), ('5', 'Right Resume')], default='1', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='userbasicinfo',
            name='whatsapp',
            field=models.CharField(blank=True, default='', max_length=400, null=True),
        ),
    ]
