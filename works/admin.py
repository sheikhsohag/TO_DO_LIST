from django.contrib import admin
from works.models import TaskModel
# Register your models here.

# admin.site.register(BookStoreModel)

class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('taskTitle', 'taskDescription','is_completed')

admin.site.register(TaskModel,TaskModelAdmin)