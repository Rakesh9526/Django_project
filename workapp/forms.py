from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Fieldset,Row,Column
from .models import Apply,Customer,FuelCharge,FoodAllowance,ItemPurchased,VendorInfo,CurrentStatus,Technicians
from django.core.exceptions import ValidationError
import re

from django.contrib.auth.models import User

# class SignUpForm(forms.ModelForm):
#     username = forms.CharField(max_length=15, required=True)
#     contact_number = forms.CharField(max_length=15, required=True)
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'contact_number', 'password']

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match.")
#         return cleaned_data

class UserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'u_contact_number': forms.TextInput(attrs={
                'placeholder' : 'Enter number with country code.'}),
            'u_whatsapp_number': forms.TextInput(attrs={
                'placeholder' : 'Enter number with country code.',
            })
        }
    def clean_u_contact_number(self):
        phone = self.cleaned_data.get('u_contact_number')
        if not re.match(r"^\+\d{10,15}$",phone):
            raise ValidationError("phonr number must be in international format(e.g./+123456789).")
        return phone
    


class DateInput(forms.DateInput):
    input_type = 'date'

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'

        widgets = {
            'estimated_date': DateInput()
        }

# class SignupForm(forms.ModelForm):
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = Technicians
#         fields =  ['name','contact_number','email','password']
         
#         widgets = {
#             'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
#             # 'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
       
#         }


#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match")
        

class FuelChargeForm(forms.ModelForm):
    class Meta:
        model = FuelCharge
        fields = '__all__'

        widgets = {
            'date': DateInput()
        }


class FoodAllowanceForm(forms.ModelForm):
    class Meta:
        model = FoodAllowance
        fields = '__all__'

        widgets = {
            'date': DateInput()
        }

class ItemPurchasedForm(forms.ModelForm):
    class Meta:
        model = ItemPurchased
        fields = '__all__'

        widgets = {
            'date': DateInput()
        }


class VendorInfoForm(forms.ModelForm):
    class Meta:
        model = VendorInfo
        fields = '__all__'

        widgets = {
            'date': DateInput(),
            'vendor_eta': DateInput()
        }

class CurrentStatusForm(forms.ModelForm):
    class Meta:
        model = CurrentStatus
        fields = '__all__'

        widgets = {
            'date': DateInput()
        }
        
    
        
