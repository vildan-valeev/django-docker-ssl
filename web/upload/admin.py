from django.contrib import admin

# Register your models here.
from upload.models import Person, City, Event

admin.site.register(City)
admin.site.register(Person)
admin.site.register(Event)