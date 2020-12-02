from django.contrib import admin
from .models import Neighbourhood,Post,Business,Profile


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['name', 'id']

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Profile, ProfileAdmin)