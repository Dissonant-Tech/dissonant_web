from django.contrib import admin
from django import forms
from dissonant_tech.models import Category, BlogPost
from pagedown.widgets import AdminPagedownWidget
from dissonant_tech.models import Category, BlogPost

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)
    search_fields = ('title',)
    fieldsets = (
            (
                None,
                {
                    'fields': ('title', 'slug',)
                    }
                ),
            )

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        widgets = {
                'content_markdown' : AdminPagedownWidget(),
                }
        exclude = ['content_markup',]

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm
    prepopulated_fields = { 'slug': ('title',) }
    list_display = ('title', 'date_publish',)
    search_fields = ('title', 'content_markdown',)
    list_filter = ('categories',)
    fieldsets = (
            (
                None,
                {
                    'fields': ('title', 'slug', 'content_markdown', 'categories', 'date_publish',)
                    }
                ),
            )


admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
