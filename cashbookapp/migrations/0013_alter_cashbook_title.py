# Generated by Django 4.0.6 on 2022-09-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0012_remove_cashbook_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashbook',
            name='title',
            field=models.CharField(error_messages={'required': '글을 입력해주세요.'}, max_length=200),
        ),
    ]