from django.contrib import admin
from .models import Guestbook
# Register your models here.

class GuestbookAdmin(admin.ModelAdmin):
    list_display=('name','email','passwd','created_at')

admin.site.register(Guestbook, GuestbookAdmin)