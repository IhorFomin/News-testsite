from django.contrib import admin

from .models import News, Category


# редактирование отображения данных в админке ( настройка админки )
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')  # отображаемые поля в админ панеле
    list_display_links = ('id', 'title')  # поля которые являються ссылками к форме
    search_fields = ('title', 'content')  # поля по которым можно производить поиск
    list_editable = ('is_published',)  # редактирование поля прямо из списка
    list_filter = ('is_published', 'category')  # поля по которым фильтруем данные


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

