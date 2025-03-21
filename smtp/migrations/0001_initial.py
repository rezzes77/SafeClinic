# Generated by Django 5.1.5 on 2025-01-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(choices=[('Директор', 'Директор'), ('Администратор', 'Администратор'), ('Стоматолог', 'Стоматолог'), ('Рентгенолог', 'Рентгенолог'), ('Педиатр', 'Педиатр'), ('Хирург', 'Хирург'), ('Пациент', 'Пациент')], max_length=100, verbose_name='Теги')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img/', verbose_name='Добавить фото')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('tags', models.CharField(choices=[('Директор', 'Директор'), ('Администратор', 'Администратор'), ('Стоматолог', 'Стоматолог'), ('Рентгенолог', 'Рентгенолог'), ('Педиатр', 'Педиатр'), ('Хирург', 'Хирург'), ('Пациент', 'Пациент')], max_length=100, verbose_name='Теги')),
                ('experience', models.CharField(max_length=30, verbose_name='Опыт работы')),
                ('about', models.TextField(verbose_name='О себе')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Телефон номер')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('Женский', 'Женский'), ('Мужской', 'Мужской')], max_length=50, verbose_name='Пол')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес')),
            ],
        ),
    ]
