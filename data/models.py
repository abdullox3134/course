from django.db import models

from config import settings


class Info(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Info'
        verbose_name_plural = 'Infos'


class Student_opinion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='student_opinions/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Student Opinion'
        verbose_name_plural = 'Student Opinions'


class Prices(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'


class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


class Connection(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Connection'
        verbose_name_plural = 'Connections'


class Contact(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    telegram = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']


class Lessons(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='lessons/')
    order = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Shu yerda `user` bo‘lishi kerak

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Textbook(models.Model):
    title = models.CharField(max_length=100)
    imege = models.ImageField(upload_to='textbooks/')
    video = models.FileField(upload_to='textbooks/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    lessons = models.ForeignKey('Lessons', on_delete=models.CASCADE)
    order = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Textbook'
        verbose_name_plural = 'Textbooks'


class Certificate(models.Model):
    image = models.ImageField(upload_to='certificates/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.full_name

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ['-created_at']