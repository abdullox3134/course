from django.contrib import admin
from .models import (
    Info, Student_opinion, Prices, FAQ, Connection, Contact,
    News, Lessons, Textbook, Certificate, Message
)

admin.site.register(Info)
admin.site.register(Student_opinion)
admin.site.register(Prices)
admin.site.register(FAQ)
admin.site.register(Connection)
admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Lessons)
admin.site.register(Textbook)
admin.site.register(Certificate)
admin.site.register(Message)
