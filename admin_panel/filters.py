import django_filters
from .models import Doctor, Patient
from datetime import date

class DoctorFilter(django_filters.FilterSet):
    AGE_CHOICES = [
        ('20-30', 'От 20 до 30'),
        ('30-40', 'От 30 до 40'),
        ('40-50', 'От 40 до 50'),
    ]

    age_range = django_filters.ChoiceFilter(
        choices=AGE_CHOICES,
        method='filter_by_age_range',
        label="Возраст"
    )

    class Meta:
        model = Doctor
        fields = ['tags', 'gender']

    def filter_by_age_range(self, queryset, name, value):
        today = date.today()
        age_ranges = {
            '20-30': (today.replace(year=today.year - 30), today.replace(year=today.year - 20)),
            '30-40': (today.replace(year=today.year - 40), today.replace(year=today.year - 30)),
            '40-50': (today.replace(year=today.year - 50), today.replace(year=today.year - 40)),
        }
        start_date, end_date = age_ranges[value]
        return queryset.filter(date_birth__range=(start_date, end_date))

#PATIENT
class PatientFilter(django_filters.FilterSet):
    AGE_CHOICES = [
        ('20-30', 'От 20 до 30'),
        ('30-40', 'От 30 до 40'),
        ('40-50', 'От 40 до 50'),
    ]

    age_range = django_filters.ChoiceFilter(
        choices=AGE_CHOICES,
        method='filter_by_age_range',
        label="Возраст"
    )

    class Meta:
        model = Patient
        fields = ['gender']

    def filter_by_age_range(self, queryset, name, value):
        today = date.today()
        age_ranges = {
            '20-30': (today.replace(year=today.year - 30), today.replace(year=today.year - 20)),
            '30-40': (today.replace(year=today.year - 40), today.replace(year=today.year - 30)),
            '40-50': (today.replace(year=today.year - 50), today.replace(year=today.year - 40)),
        }
        start_date, end_date = age_ranges[value]
        return queryset.filter(date_birth__range=(start_date, end_date))