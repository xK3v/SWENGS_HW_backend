from django.contrib import admin
from . import models

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Student, StudentAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Department,DepartmentAdmin)

