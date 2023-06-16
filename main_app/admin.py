from django.contrib import admin
# import your models here
from .models import Poke, Feeding, Toy

# Register your models here
admin.site.register(Poke)
admin.site.register(Feeding)
admin.site.register(Toy)