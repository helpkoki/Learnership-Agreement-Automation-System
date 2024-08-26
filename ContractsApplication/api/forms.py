from django import forms
from .models import Contracts_completed

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contracts_completed
        fields = [
            'name', 
            'street_number_and_name', 'city', 'state_or_province', 'postal_code', 'country',
            'phone_cell', 'phone_home', 'email',
            'school', 'school_email', 'school_mobile', 'school_contact_person',
            'company_name', 
            'company_street_number_and_name', 'company_city', 'company_state_or_province',
            'company_postal_code', 'company_country', 'intern_supervisor',
            'supervisor_phone', 'supervisor_email', 
            'start_date', 'end_date', 'intern_title', 'duties_description',
            'hours', 'intern_signature', 'hr_signature'
        ]
        
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'duties_description': forms.Textarea(attrs={'rows': 4}),
            'hours': forms.TextInput(attrs={'placeholder': 'Enter hours'}),
            'phone_cell': forms.TextInput(attrs={'class': 'phone-input', 'placeholder': '+123 456 7890'}),
            'phone_home': forms.TextInput(attrs={'class': 'phone-input', 'placeholder': '+123 456 7890'}),
            'school_mobile':forms.TextInput(attrs={'class': 'phone-input', 'placeholder': '+123 456 7890'}),
            'school_contact_person':forms.TextInput(attrs={'class': 'phone-input', 'placeholder': '+123 456 7890'}),
            'supervisor_phone':forms.TextInput(attrs={'class': 'phone-input', 'placeholder': '+123 456 7890'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'supervisor_email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'school_email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'intern_title': forms.Select(choices=[
                ('Intern', 'Intern'),
                ('Student', 'Student'),
                ('Learner', 'Learner'),
                ('Graduate', 'Graduate'),
                ('Transferee', 'Transferee')
            ]),
        }
