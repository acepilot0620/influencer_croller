from django.contrib import admin
from .models import Youtube_result,Search,Instagram_result

# Register your models here.
admin.site.register(Youtube_result)
admin.site.register(Instagram_result)
admin.site.register(Search)
