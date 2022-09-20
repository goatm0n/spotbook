from django.contrib import admin
from .models import Clip, ClipLike

class ClipLikeAdmin(admin.TabularInline):
    model = ClipLike

class ClipAdmin(admin.ModelAdmin):
    inlines = [ClipLikeAdmin]
    class Meta:
        model = Clip


admin.site.register(Clip, ClipAdmin)
