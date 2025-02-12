from rest_framework import serializers
from .models import (
    Info, Student_opinion, Prices, FAQ, Connection, Contact,
    News, Lessons, Textbook, Certificate, Message
)


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'


class StudentOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_opinion
        fields = '__all__'


class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'


class TextbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textbook
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
