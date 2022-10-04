# Generated by Django 4.1.1 on 2022-09-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('dialogue', models.CharField(max_length=200)),
                ('villian', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
