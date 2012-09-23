from django.contrib import admin

from ciem.apps.articles.models import *

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}


class ArticleAdmin(admin.ModelAdmin):
	fieldsets = (
		('Article content', {
			'fields': ('title', 'body', 'category', 'tags', 'author')
		}),
		('Publication info', {
			'classes': ('collapse',),
			'fields': ('status', 'publish_date')
		}),
		('Advanced', {
			'classes': ('collapse',),
			'fields': ('featured',  'summary', 'snippet', 'slug',)
		}),
	)
	radio_fields = {'status': admin.VERTICAL}
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ('tags', 'title', 'body')
	list_display = ('title', 'tags', 'publish_date', 'get_absolute_url', 'status')
	list_filter = ('publish_date', 'status', 'category',)
	date_hierarchy = 'publish_date'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)