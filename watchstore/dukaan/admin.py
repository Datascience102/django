from django.contrib import admin

from .models import Watch

# creating Model Admin to show it in Admin panel

class WatchAdmin(admin.ModelAdmin):
    list_display = ('title','publish_date','company','price','stock')




# register Watch & watchadmin to show them in admin panel
admin.site.register(Watch,WatchAdmin)
