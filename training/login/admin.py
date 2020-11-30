from django.contrib import admin

# Register your models here.

from login.models import Member


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Member,AuthorAdmin)