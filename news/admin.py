from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


# редактирование отображения данных в админке ( настройка админки )
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')  # отображаемые поля в админ панеле
    list_display_links = ('id', 'title')  # поля которые являються ссылками к форме
    search_fields = ('title', 'content')  # поля по которым можно производить поиск
    list_editable = ('is_published',)  # редактирование поля прямо из списка
    list_filter = ('is_published', 'category')  # поля по которым фильтруем данные
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')  # поля которые выводяться внутри новости ( редактируемые поля )
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')  # поля только для чтения
    save_on_top = True  # панель сохранения данных создаеться вверху страницы

    def get_photo(self, obj):
        """
        Отображение изображение в админке (не как ссылка)
        :param obj:
        :return: html код изображения
        """
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '-'

    get_photo.short_description = 'Миниатюра'  # изменение названия поля get_photo


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'

