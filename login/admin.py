# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import category


# Register your models here.
class categoryadmin(admin.ModelAdmin):
	list_display=["user","customer"]

admin.site.register(category,categoryadmin)