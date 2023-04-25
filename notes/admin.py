from django.contrib import admin

# Register your models here.
from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = (
        'title',
    )

    list_display = (
        'title',
        'content',
        'created_by',
        'created_date',
        'published_date',
    )


admin.site.register(Note, NoteAdmin)