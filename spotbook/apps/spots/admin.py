from django.contrib import admin
from .models import Spot, SpotLike, SpotMapIcon
from leaflet.admin import LeafletGeoAdmin

class SpotLikeAdmin(admin.TabularInline):
    model = SpotLike

class SpotAdmin(LeafletGeoAdmin):
    inlines = [SpotLikeAdmin]

admin.site.register(Spot, SpotAdmin)
admin.site.register(SpotMapIcon)
