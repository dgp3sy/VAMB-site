from django import forms
from hours.models import VolunteerLog
class VolunteerLogForms(forms.ModelForm):
    class Meta:
        model = VolunteerLog
        fields = ['first_name', 'last_name', 'computing_id', 'hours']
    # def __init__(self, *args, **kwargs):
    #     super(VolunteerLogForms, self).__init__(*args, **kwargs)
