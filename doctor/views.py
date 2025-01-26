from rest_framework.response import Response
from client.models import Appointment
from .serializers import DoctorCalendarSerializer
from datetime import datetime, timedelta
from rest_framework import viewsets

###################################
########КАЛЕНДАРЬ##################
###################################

class DoctorCalendarViewSet(viewsets.ViewSet):
    """
    API для получения записей врача с фильтрацией по дням, неделям и месяцам.
    """
    def list(self, request, *args, **kwargs):
        doctor_id = request.query_params.get('doctor')
        period = request.query_params.get('period')  # day, week, month

        if not doctor_id:
            return Response({"error": "Параметр 'doctor' обязателен."}, status=400)

        today = datetime.today().date()

        if period == "day":
            start_date = today
            end_date = today
        elif period == "week":
            start_date = today - timedelta(days=today.weekday())
            end_date = start_date + timedelta(days=6)
        elif period == "month":
            start_date = today.replace(day=1)
            if today.month == 12:
                end_date = today.replace(year=today.year + 1, month=1, day=1) - timedelta(days=1)
            else:
                end_date = today.replace(month=today.month + 1, day=1) - timedelta(days=1)
        else:
            return Response({"error": "Неверный параметр 'period'. Используйте 'day', 'week' или 'month'."}, status=400)

        appointments = Appointment.objects.filter(doctor_id=doctor_id, date__range=(start_date, end_date)).order_by('date', 'time')

        count = appointments.count()

        serialized_appointments = []
        previous_appointment = None

        for appointment in appointments:
            serialized = DoctorCalendarSerializer(appointment).data

            if previous_appointment:
                serialized['previous'] = {
                    "date": previous_appointment.date,
                    "time": previous_appointment.time
                }
            else:
                serialized['previous'] = None

            previous_appointment = appointment
            serialized_appointments.append(serialized)

        for i in range(len(serialized_appointments) - 1):
            serialized_appointments[i]['next'] = {
                "date": serialized_appointments[i + 1]['date'],
                "time": serialized_appointments[i + 1]['time']
            }
        if serialized_appointments:
            serialized_appointments[-1]['next'] = None

        data = {
            "count": count,
            "appointments": serialized_appointments
        }

        return Response(data)