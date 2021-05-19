from django.contrib import admin
from .models import Card,Category


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    list_display_links = ("title", )
    ordering = ("-created_at",)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)




