from django.contrib import admin
from django import forms
from blog.models import Category, Article
from pagedown.widgets import AdminPagedownWidget

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

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
                'content_markdown' : AdminPagedownWidget(),
                }
        exclude = ['content_markup',]

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    prepopulated_fields = { 'slug': ('title',) }
    list_display = ('title', 'author', 'date_publish',)
    search_fields = ('title', 'content_markdown',)
    list_filter = ('categories',)
    readonly_fields = ('date_publish',)
    fieldsets = (
            (
                None,
                {
                    'fields': ('title', 'slug', 'content_markdown', 'categories',)
                    }
                ),
            )
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
