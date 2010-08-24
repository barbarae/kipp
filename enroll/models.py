from datetime import datetime
from django.db import models


class Enrollment(models.Model):
    """Records an online enrollment in the academy."""
    student_name = models.CharField(max_length=255)
    address1 = models.CharField('address', max_length=255)
    address2 = models.CharField('address', max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    home_phone = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    current_grade = models.CharField(max_length=255)
    current_school = models.CharField(max_length=255)
    parent_name = models.CharField(max_length=255, blank=True)
    parent_address1 = models.CharField('address', max_length=255)
    parent_address2 = models.CharField('address', max_length=255, blank=True)
    parent_city = models.CharField(max_length=100)
    parent_state = models.CharField(max_length=2)
    parent_zip = models.CharField(max_length=5)
    parent_home_phone = models.CharField('home phone', max_length=255)
    parent_cell_phone = models.CharField('cell phone', max_length=255, blank=True)
    parent_work_phone = models.CharField('work phone', max_length=255, blank=True)
    parent_email_address = models.EmailField('e-mail address', max_length=75, blank=True)
    time_submitted = models.DateTimeField(default=datetime.now, editable=False)
