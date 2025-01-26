from tkinter.constants import CASCADE

from django.db import models
from django.core.exceptions import ValidationError


###################
#СПИСОК ВРАЧЕЙ#####
###################

class Doctor(models.Model):
    image = models.ImageField(upload_to='doctor-img/', verbose_name='Добавить фото')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    date_birth = models.DateField(verbose_name='Дата рождение')
    tags = models.CharField(max_length=100, verbose_name='Теги', choices=[
        ('Директор', 'Директор'),
        ('Администратор', 'Администратор'),
        ('Стоматолог', 'Стоматолог'),
        ('Рентгенолог', 'Рентгенолог'),
        ('Педиатр', 'Педиатр'),
        ('Хирург', 'Хирург'),
        ('Пациент', 'Пациент'),
    ])
    gender = models.CharField(max_length=50, verbose_name='Пол', choices=[
        ('Женский','Женский'),
        ('Мужской','Мужской'),
    ])
    email = models.EmailField()
    address = models.CharField(max_length=300, verbose_name='Адрес')
    phone_number = models.CharField(max_length=20, verbose_name='Телефон номер')


    def __str__(self):
        return self.full_name

###################
#СПИСОК ФИЛИАЛОВ###
###################
class Director(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название филиала')
    address = models.CharField(max_length=300, verbose_name='Адрес')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name='Директор', default=1)
    phone_number = models.CharField(max_length=12, verbose_name='Телефон номер')

    def __str__(self):
        return self.name

###################
#СПИСОК ПАЦИЕНТОВ##
###################

class Patient(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    phone_number = models.CharField(max_length=12, verbose_name='Телефон номер')
    address = models.CharField(max_length=300, verbose_name='Адрес')
    appointment = models.ForeignKey('admin_panel.Doctor', on_delete=models.CASCADE, verbose_name='Запись к врачу', related_name="patient_appointments")
    date_appointment = models.DateField(verbose_name='Дата записи')
    gender = models.CharField(max_length=50, verbose_name='Пол', choices=[
        ('Женский', 'Женский'),
        ('Мужской', 'Мужской'),
    ])
    date_birth = models.DateField(verbose_name='Дата рождение')
    complaints = models.TextField(verbose_name='Жалобы')
    time = models.CharField(max_length=100, verbose_name='Время', choices=[
        ('08:00-09:00', '08:00-09:00'),
        ('09:00-10:00', '09:00-10:00'),
        ('10:00-11:00', '10:00-11:00'),
        ('11:00-12:00', '11:00-12:00'),
        ('12:00-13:00', '12:00-13:00'),
        ('13:00-14:00', '13:00-14:00'),
        ('14:00-15:00', '14:00-15:00'),
        ('15:00-16:00', '15:00-16:00'),
        ('16:00-17:00', '16:00-17:00'),
        ('17:00-18:00', '17:00-18:00'),
    ])

    def __str__(self):
        return self.full_name

    def validate_unique_appointment(self):
        if Patient.objects.filter(appointment=self.appointment, date_appointment=self.date_appointment, time=self.time).exists():
            raise ValidationError(f'Запись на {self.date_appointment} в {self.time} уже занята.')

    def save(self, *args, **kwargs):
        self.validate_unique_appointment()
        super().save(*args, **kwargs)

    def clean(self):
        if Patient.objects.filter(appointment=self.appointment, date_appointment=self.date_appointment,
                                  time=self.time).exists():
            raise ValidationError(f'Запись на {self.date_appointment} в {self.time} уже занята.')


###################
########УСЛУГИ#####
###################


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    def __str__(self):
        return self.name

class Service(models.Model):
    image = models.ImageField(upload_to='service-img/', verbose_name='Фото')
    name = models.CharField(max_length=100, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание услгу')
    price = models.CharField(max_length=30, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name="services", null=True, blank=True)

    def __str__(self):
        return self.name

