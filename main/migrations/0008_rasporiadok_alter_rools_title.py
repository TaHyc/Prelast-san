# Generated by Django 4.2 on 2023-05-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_image_alter_posters_kartinka'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rasporiadok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Распорядок дня',
                'verbose_name_plural': 'Распорядок дней',
            },
        ),
        migrations.AlterField(
            model_name='rools',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Название'),
        ),
    ]
