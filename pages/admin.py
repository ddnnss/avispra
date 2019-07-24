from django.contrib import admin
from .models import *

class ImagesInline (admin.TabularInline):
    model = ItemImage
    readonly_fields = ('image_tag', )
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']
    #list_display = [field.name for field in Item._meta.fields]
    inlines = [ImagesInline]

    exclude = ['name_slug','views', ] #не отображать на сранице редактирования
    class Meta:
        model = Item

admin.site.register(AboutPageClients)
admin.site.register(AboutPageWork)
admin.site.register(AboutSlider)
admin.site.register(Services)
admin.site.register(Page)
admin.site.register(Category)
admin.site.register(Item,ItemAdmin)
admin.site.register(ItemImage)
admin.site.register(Forms)



