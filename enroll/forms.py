from django import forms

from kipp.enroll.models import Enrollment


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        exclude = ('time_submitted',)
