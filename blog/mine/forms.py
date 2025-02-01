from django import forms
from .models import ChaiVarity

# modelchoicefield can query inside our existing model and
# show data according to our need and make a dropdown chaoicefield
class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(),
                                         label='Select Chai Varity')