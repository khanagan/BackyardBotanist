from django.contrib import admin

# Register your models here.
from .models import Plant, User, ConservationRank, Pictures, Group, Subgroup, Location, ListingStatus, Sighting, \
    ChangePassword, PlantLocation

admin.site.register(Plant)
admin.site.register(User)
admin.site.register(ConservationRank)
admin.site.register(Group)
admin.site.register(Subgroup)
admin.site.register(Pictures)
admin.site.register(Location)
admin.site.register(ListingStatus)
admin.site.register(Sighting)
admin.site.register(ChangePassword)
admin.site.register(PlantLocation)
