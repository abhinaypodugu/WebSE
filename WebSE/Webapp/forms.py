from django import forms
from Webapp.models import FoodDonationModel
from django.forms import ModelForm
# class FoodDonationForm(forms.ModelForm):
#     # TODO: Define other fields here
#
#     class Meta:
#         model = FoodDonationModel
#         fields = ['name_fd','Location_fd','phone_fd','Amount_fd','FoodType_fd','Reason_fd']
#
#     # def __init__(self, *args, **kwargs):
#     #     super(Form, self).__init__(*args, **kwargs)
#
#     def clean(self):
#         cleaned_data = super(Form, self).clean()
#         return cleaned_data
# #
# class FoodDonationForm(forms.ModelForm):
#     name_fd = forms.CharField(max_length=256)
#     phone_fd = forms.CharField(max_length=256)
#     Location_fd = forms.CharField(widget=forms.Textarea)
#     Amount_fd  = forms.CharField(max_length=256)
#     FoodType_fd = forms.CharField(max_length=256)
#     Reason_fd = forms.CharField(max_length=256)
class FoodDonationForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = FoodDonationModel
        fields = ['name_fd','phone_fd','Location_fd','Amount_fd','FoodType_fd','Reason_fd']

   
