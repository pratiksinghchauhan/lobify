# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import contact,messcanteen,diet,urlshort,credittable

# Register your models here.



class mess_canteenadmin(admin.ModelAdmin):
	list_display=["incharge","messcanteen"]

class dietadmin(admin.ModelAdmin):
	list_display=["messname","customer","amount","remarks","verified","ts"]

class contactadmin(admin.ModelAdmin):
	list_display=["username","mobileno"]

class urlshortadmin(admin.ModelAdmin):
	list_display=["dietplan","link"]

class creditadmin(admin.ModelAdmin):
	list_display=["messname","customer","credit"]


admin.site.register(credittable,creditadmin)
admin.site.register(messcanteen,mess_canteenadmin)
admin.site.register(diet,dietadmin)
admin.site.register(contact,contactadmin)
admin.site.register(urlshort,urlshortadmin)



