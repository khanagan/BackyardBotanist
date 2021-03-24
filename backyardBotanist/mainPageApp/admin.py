from django.contrib import admin

# Register your models here.
from .models import Plant, User, ConservationRank, Pictures, Group, Subgroup, Location
admin.site.register(Plant)
admin.site.register(User)
admin.site.register(ConservationRank)
admin.site.register(Group)
admin.site.register(Subgroup)
admin.site.register(Pictures)
admin.site.register(Location)

