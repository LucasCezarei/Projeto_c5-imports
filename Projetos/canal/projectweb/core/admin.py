from django.contrib import admin
from .models import Roupas
# Register your models here.

#registro de roupas do models
@admin.register(Roupas)
class RoupasAdmin(admin.ModelAdmin):
    list_display = ['id', 'marca', 'descricao', 'user']

