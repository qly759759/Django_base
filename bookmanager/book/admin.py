from django.contrib import admin

from book.models import BookInfo, People
# Register your models here.
admin.site.register(BookInfo)
admin.site.register(People)
