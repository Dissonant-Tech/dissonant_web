from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from blog.models import Category, Article


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
            'content': AdminPagedownWidget(
                css=(
                    'css/pagedown.css',
                    'pagedown/demo/browser/demo.css',
                    'css/article.css')
                ),
        }
        exclude = []


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'date_publish',)
    search_fields = ('title', 'content',)
    list_filter = ('categories', 'date_publish')
    fieldsets = (
        (
            None,
            {
                'fields': (
                    'title',
                    'slug',
                    'cover_image',
                    'published',
                    'date_publish',
                    'content',
                    'categories',
                    )
            }
        ),
    )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
