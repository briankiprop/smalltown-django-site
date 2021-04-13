from django.contrib import admin
from .models import notices,news_updates,events_model
# Register your models here.
class news_udatesAdmin(admin.ModelAdmin):
    # ...
    list_display = ('headline', 'author')

class events_modelAdmin(admin.ModelAdmin):
    # ...
    list_display = ('date', 'headline')

class noticesAdmin(admin.ModelAdmin):
    # ...
    list_display = ('pdf_file', 'description')

admin.site.register(news_updates,news_udatesAdmin)
admin.site.register(events_model,events_modelAdmin)
admin.site.register(notices,noticesAdmin)