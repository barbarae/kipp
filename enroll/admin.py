from django.contrib import admin
from enroll.models import Enrollment

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'time_submitted',)


admin.site.register(Enrollment, EnrollmentAdmin)

