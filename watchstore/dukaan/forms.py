from django import forms
from .models import Watch

class WatchForm(forms.ModelForm):
    class Meta:
	    model = Watch
		fields = ["title","company","image","description","price","stock"]
		