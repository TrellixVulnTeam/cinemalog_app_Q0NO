# Generated by Django 2.2.3 on 2019-07-22 10:27

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=30, null=True, verbose_name='نام کاربری')),
                ('phone', models.CharField(max_length=11, verbose_name='phone')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='image')),
                ('address', models.TextField(max_length=300, verbose_name='address')),
                ('password', models.CharField(max_length=300, verbose_name='گذرواژه')),
                ('notification_status', models.BooleanField(default=False, verbose_name='notification_status')),
                ('created_at', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='create_at')),
                ('updated_at', django_jalali.db.models.jDateTimeField(blank=True, null=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField(max_length=500, verbose_name='token')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='user_id')),
            ],
            options={
                'verbose_name': 'UserToken',
                'verbose_name_plural': 'UserTokens',
            },
        ),
    ]
