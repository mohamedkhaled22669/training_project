from django.contrib import admin

# Register your models here.

from home.models import Nodes


class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Nodes,AuthorAdmin)