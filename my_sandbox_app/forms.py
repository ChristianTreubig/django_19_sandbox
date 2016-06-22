from django import forms
from my_sandbox_app.models import Resident

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ["first_name", "last_name", "age", "location"]