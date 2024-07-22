from django.contrib import admin
from .models import Students
from .models import Websites
from .models import Barcode




models_list = [Students] 
admin.site.register(models_list)
admin.site.register(Websites)
admin.site.register(Barcode)
