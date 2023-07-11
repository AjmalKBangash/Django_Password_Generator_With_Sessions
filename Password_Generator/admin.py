from django.contrib import admin
from django.contrib.sessions.models import Session

# Register your models here.

# if you want to save decoded data in django-admin
# class SessionAdmin(ModelAdmin):
#     def _session_data(self, obj):
#         return obj.get_decoded()
#     list_display = ['session_key', '_session_data', 'expire_date']
# admin.site.register(Session, SessionAdmin)
admin.site.register(Session)

