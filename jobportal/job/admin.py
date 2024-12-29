from django.contrib import admin
from .models import CustomUser
from .models import Company
from .models import Job

admin.site.register(CustomUser)
admin.site.register(Company)
admin.site.register(Job)

# Register your models here.
