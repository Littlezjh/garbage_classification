# Generated by Django 2.2.3 on 2019-07-19 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190718_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='credits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='phonenumber',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='openid',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.CreateModel(
            name='ClassificationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagepath', models.CharField(max_length=100)),
                ('imagedate', models.CharField(max_length=50)),
                ('imagekind', models.CharField(max_length=20)),
                ('imagetype', models.CharField(max_length=20)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.UserInfo', to_field='openid')),
            ],
        ),
    ]
