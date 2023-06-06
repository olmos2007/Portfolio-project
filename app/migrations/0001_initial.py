# Generated by Django 4.2.1 on 2023-06-06 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='My_images')),
                ('name_surname', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=13)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('year', models.DateField()),
                ('about_me', models.TextField()),
            ],
            options={
                'verbose_name': 'Me',
                'verbose_name_plural': 'We',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio_images')),
                ('name', models.CharField(max_length=200)),
                ('about', models.TextField()),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('count', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Statistic',
                'verbose_name_plural': 'Statistics',
            },
        ),
    ]