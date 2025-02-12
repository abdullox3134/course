from rest_framework import generics, permissions
from django.core.exceptions import PermissionDenied
from .models import (
    Info, Student_opinion, Prices, FAQ, Connection, Contact,
    News, Lessons, Textbook, Certificate, Message
)
from .serializers import (
    InfoSerializer, StudentOpinionSerializer, PricesSerializer, FAQSerializer,
    ConnectionSerializer, ContactSerializer, NewsSerializer, LessonsSerializer,
    TextbookSerializer, CertificateSerializer, MessageSerializer
)


# Info uchun List va Detail API
class InfoListView(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class InfoDetailView(generics.RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    lookup_field = 'id'


# StudentOpinion faqat list bo'lishi kerak
class StudentOpinionListView(generics.ListAPIView):
    queryset = Student_opinion.objects.all()
    serializer_class = StudentOpinionSerializer


# Prices faqat list bo'lishi kerak
class PricesListView(generics.ListAPIView):
    queryset = Prices.objects.all()
    serializer_class = PricesSerializer


# FAQ uchun List va Detail API
class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class FAQDetailView(generics.RetrieveAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    lookup_field = 'id'


# Connection faqat POST qilish kerak
class ConnectionCreateView(generics.CreateAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    permission_classes = [permissions.AllowAny]


# Contact faqat list bo'lishi kerak
class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# News uchun List va Detail API
class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'


# Lessons faqat List va Detail bo'lishi kerak
class LessonsListView(generics.ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsDetailView(generics.RetrieveAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    lookup_field = 'id'


class TextbookListView(generics.ListAPIView):
    serializer_class = TextbookSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Textbook.objects.filter(user=user).distinct()  # Faqat userga tegishli darsliklarni qaytarish
        return Textbook.objects.none()


class TextbookDetailView(generics.RetrieveAPIView):
    serializer_class = TextbookSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Textbook.objects.filter(user=user)
        return Textbook.objects.none()

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("Sizga tegishli bo‘lmagan darslikni ko‘rish huquqingiz yo‘q!")
        return obj


# Certificate faqat foydalanuvchiga tegishlisi chiqishi kerak
class CertificateListView(generics.ListAPIView):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        return Certificate.objects.filter(user=self.request.user)


class CertificateDetailView(generics.RetrieveAPIView):
    serializer_class = CertificateSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Certificate.objects.filter(user=self.request.user)



class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
