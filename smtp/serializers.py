from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.crypto import get_random_string
from rest_framework import serializers
from .models import Register, Login

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'

    def create(self, validated_data):
        random_password = get_random_string(length=10)
        username = validated_data.get('username')
        email = validated_data.get('email')

        user = Register.objects.create(**validated_data)

        Login.objects.create(username=username, password=random_password)

        # Подготовка HTML-письма с использованием шаблона
        context = {
            'username': username,
            'password': random_password,
            'clinic_name': 'SafeClinic',
            'support_email': 'support@safeclinic.com'
        }

        html_content = render_to_string('emails/registration_email.html', context)
        plain_message = strip_tags(html_content)
        email_message = EmailMessage(
            subject="Добро пожаловать в SafeClinic!",
            body=html_content,
            from_email='abdugood03@gmail.com',
            to=[email],
        )
        email_message.content_subtype = "html"
        email_message.send(fail_silently=False)

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        try:
            user = Login.objects.get(username=username, password=password)
        except Login.DoesNotExist:
            raise serializers.ValidationError("Неверный логин или пароль")

        return data
