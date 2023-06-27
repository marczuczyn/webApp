from django.contrib import admin
from .models import Ankieta


@admin.register(Ankieta)
class AnkietaAdmin(admin.ModelAdmin):
    list_display = ["id", "wiek", "wzrost", "plec", "kolor", "created_at", "updated_at"]
