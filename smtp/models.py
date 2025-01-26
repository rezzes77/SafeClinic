from django.db import models

class Register(models.Model):
    image = models.ImageField(upload_to='img/', verbose_name='Добавить фото')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    username = models.CharField(max_length=100, unique=True)
    tags = models.CharField(max_length=100, verbose_name='Теги', choices=[
        ('Директор', 'Директор'),
        ('Администратор', 'Администратор'),
        ('Стоматолог', 'Стоматолог'),
        ('Рентгенолог', 'Рентгенолог'),
        ('Педиатр', 'Педиатр'),
        ('Хирург', 'Хирург'),
        ('Пациент', 'Пациент'),
    ])
    experience = models.CharField(max_length=30, verbose_name='Опыт работы')
    about = models.TextField(verbose_name='О себе')
    phone_number = models.CharField(max_length=20, verbose_name='Телефон номер')
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=50, verbose_name='Пол', choices=[
        ('Женский', 'Женский'),
        ('Мужской', 'Мужской'),
    ])
    address = models.CharField(max_length=300, verbose_name='Адрес')

    def __str__(self):
        return self.full_name

class Login(models.Model):
    tags = models.CharField(max_length=100, verbose_name='Теги', choices=[
        ('Директор', 'Директор'),
        ('Администратор', 'Администратор'),
        ('Стоматолог', 'Стоматолог'),
        ('Рентгенолог', 'Рентгенолог'),
        ('Педиатр', 'Педиатр'),
        ('Хирург', 'Хирург'),
        ('Пациент', 'Пациент'),
    ])
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)
