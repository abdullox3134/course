from django.urls import path
from .views import (
    InfoListView, InfoDetailView,
    StudentOpinionListView, PricesListView,
    FAQListView, FAQDetailView,
    ConnectionCreateView, ContactListView,
    NewsListView, NewsDetailView,
    LessonsListView, LessonsDetailView,
    TextbookListView, TextbookDetailView,
    CertificateListView, CertificateDetailView, MessageListCreateView,
)


urlpatterns = [
    # Info
    path('info/', InfoListView.as_view(), name='info-list'),
    path('info/<int:id>/', InfoDetailView.as_view(), name='info-detail'),

    # Student Opinion
    path('student-opinion/', StudentOpinionListView.as_view(), name='student-opinion-list'),

    # Prices
    path('prices/', PricesListView.as_view(), name='prices-list'),

    # FAQ
    path('faq/', FAQListView.as_view(), name='faq-list'),
    path('faq/<int:id>/', FAQDetailView.as_view(), name='faq-detail'),

    # Connection (faqat POST)
    path('connection/', ConnectionCreateView.as_view(), name='connection-create'),

    # Contact
    path('contact/', ContactListView.as_view(), name='contact-list'),

    # News
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:id>/', NewsDetailView.as_view(), name='news-detail'),

    # Lessons
    path('lessons/', LessonsListView.as_view(), name='lessons-list'),
    path('lessons/<int:id>/', LessonsDetailView.as_view(), name='lessons-detail'),

    # Textbook (faqat foydalanuvchiga tegishli)
    path('textbooks/', TextbookListView.as_view(), name='textbook-list'),
    path('textbooks/<int:id>/', TextbookDetailView.as_view(), name='textbook-detail'),

    # Certificate (faqat foydalanuvchiga tegishli)
    path('certificates/', CertificateListView.as_view(), name='certificate-list'),
    path('certificates/<int:id>/', CertificateDetailView.as_view(), name='certificate-detail'),

    path('messages/', MessageListCreateView.as_view(), name='messages-list-create'),
]
