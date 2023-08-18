from django.contrib import admin
from .models   import milk, cow, Warehouse, food, foodcategory, group, report, shekara
# Register your models here.


admin.site.register([milk, cow, Warehouse,food, foodcategory, group, report, shekara])
