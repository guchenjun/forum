# Generated by Django 2.0.5 on 2018-06-17 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20180617_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatgoryName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_id', models.CharField(max_length=3)),
                ('cat_name', models.CharField(max_length=32)),
            ],
        ),
    ]