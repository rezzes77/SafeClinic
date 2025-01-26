from django.db import models

from django.contrib.auth.models import AbstractUser, Group, Permission


###################
####ЗАПИСАТЬСЯ#####
###################

from django.core.exceptions import ValidationError
from django.db import models

class Appointment(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    service = models.ForeignKey('admin_panel.Service', on_delete=models.CASCADE)
    doctor = models.ForeignKey('admin_panel.Doctor', on_delete=models.CASCADE, verbose_name='Запись к врачу', related_name="appointments")
    date = models.DateField(verbose_name='Дата записи')
    complains = models.TextField(verbose_name='Жалобы')
    phone_number = models.CharField(verbose_name='Телефон номер', max_length=15, unique=True)
    address = models.CharField(max_length=100, verbose_name='Адрес')
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
        if Appointment.objects.filter(doctor=self.doctor, date=self.date, time=self.time).exists():
            raise ValidationError(f'Запись на {self.date} в {self.time} уже занята.')

    def save(self, *args, **kwargs):
        self.validate_unique_appointment()
        super().save(*args, **kwargs)
