# Generated by Django 4.1.5 on 2023-10-19 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'Категории новостей', 'verbose_name_plural': 'Добавить Категории новостей'},
        ),
        migrations.AlterModelOptions(
            name='newsmodel',
            options={'verbose_name': 'Добавить новосит', 'verbose_name_plural': 'Добавить новости тут'},
        ),
    ]
