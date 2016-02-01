from django.contrib import admin
from dissonant_website.models import Project


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name',)
    search_fields = ('name',)
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'name',
                    'description',
                    'link',
                    'slug',
                    )
            }
        ),
    )

admin.site.register(Project, ProjectAdmin)
