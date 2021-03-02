# Generated by Django 2.2.4 on 2021-03-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0, verbose_name='年龄'),
        ),
        migrations.AddField(
            model_name='user',
            name='hobby',
            field=models.CharField(default='study', max_length=32, verbose_name='兴趣爱好'),
        ),
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.CharField(max_length=32, null=True, verbose_name='个人简介'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='主键'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.IntegerField(verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, verbose_name='用户名'),
        ),
    ]