from django.contrib import admin

from task.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name", )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content", )
