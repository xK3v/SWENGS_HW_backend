from django.contrib import admin
from . import models

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Student, StudentAdmin)


class DepartementAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Departement,DepartementAdmin)

