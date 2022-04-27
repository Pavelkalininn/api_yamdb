from django.contrib import admin

from .models import Genre, Title, GenreTitle, Category


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'category')
    search_fields = ('name',)
    list_filter = ('year',)
    empty_value_display = '-пусто-'


admin.site.register(Title, TitleAdmin)
admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(GenreTitle)