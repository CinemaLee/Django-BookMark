from django.contrib import admin
from .models import Guestbook,Fcuser
# Register your models here.

class GuestbookAdmin(admin.ModelAdmin):
    list_display=('name','email','passwd','created_at')

class FcuserAdmin(admin.ModelAdmin):
    list_display=('username', 'useremail', 'password')

admin.site.register(Guestbook, GuestbookAdmin)
admin.site.register(Fcuser, FcuserAdmin)