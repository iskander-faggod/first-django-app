from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import News, Category


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = NewsAdminForm




class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = (
        'id',
        'title',
        'category',
        'created_at',
        'updated_at',
        'is_published'
    )
    list_filter = ('is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)


class Admin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, Admin)
