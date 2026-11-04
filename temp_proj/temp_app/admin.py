from django.contrib import admin

from .models import Person, Dog, Cat

admin.site.register(Person)
admin.site.register(Dog)
admin.site.register(Cat)