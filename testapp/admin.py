from django.contrib import admin
# from mptt.admin import MPTTModelAdmin
# Модуй для реализации перетаскивания вложенстей в админке
from mptt.admin import DraggableMPTTAdmin
from .models import Rubric, Article

# Реализация отступов в админке через класс вместо MPTT_ADMIN_LEVEL_INDENT = 20 в файле настроек
# class CustomMPTTModelAdmin(MPTTModelAdmin):
#     # specify pixel amount for this ModelAdmin only:
#     mptt_level_indent = 20

# admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
admin.site.register(Article)
