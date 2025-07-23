from django.contrib import admin

# Register your models here.
from .models import Emp, Testimonial,Feedback
class EmpAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'emp_id', 'emp_email', 'phone', 'working', 'address', 'department')
    list_editable = ('working', 'emp_id','phone')
    search_fields=('name', 'emp_id')
    list_filter = ('working',)
admin.site.register(Emp, EmpAdmin)
admin.site.register(Testimonial)

class FeedbackAdmin(admin.ModelAdmin):
    list_display=('name', 'email','feedback')
admin.site.register(Feedback, FeedbackAdmin)