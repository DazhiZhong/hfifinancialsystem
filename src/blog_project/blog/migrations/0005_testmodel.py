# Generated by Django 2.2.4 on 2019-09-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_envvaribles'),
    ]

    operations = [
        migrations.CreateModel(
            name='testmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('活该', models.IntegerField(default=1, null=True)),
            ],
        ),
    ]
