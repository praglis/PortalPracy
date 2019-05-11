from django.contrib import admin

from .models import Company, Agency, Offert, Tag, Application

admin.site.register(Company)
admin.site.register(Agency)
admin.site.register(Offert)
admin.site.register(Tag)
admin.site.register(Application)
