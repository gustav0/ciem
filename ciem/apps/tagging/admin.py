from django.contrib import admin
from ciem.apps.tagging.models import Tag, TaggedItem
from ciem.apps.tagging.forms import TagAdminForm

class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm

admin.site.register(TaggedItem)
admin.site.register(Tag, TagAdmin)




