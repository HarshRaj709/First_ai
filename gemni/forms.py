from django import forms
from django.contrib.auth.models import User

class InfoForm(forms.Form):
    VISITOR_CHOICES = [
        ('student', 'Student'),
        ('couple', 'Couple'),
        ('family', 'Family'),
        ('solo', 'Solo Traveler'),
        ('business', 'Business Traveler'),
    ]
    INTEREST_CHOICES = [
        ('heritage', 'Heritage & History'),
        ('nature', 'Nature & Parks'),
        ('culture', 'Cultural & Arts'),
        ('food', 'Food & Restaurants'),
        ('shopping', 'Shopping'),
        ('adventure', 'Adventure & Fun'),
    ]
    TIME_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening/Night'),
    ]
    BUDGET_CHOICES = [
        ('low', 'Low Budget'),
        ('medium', 'Medium Budget'),
        ('luxury', 'Luxury Budget'),
    ]
    TRANSPORT_CHOICES = [
        ('walking', 'Walking Distance'),
        ('bike', 'Bike'),
        ('car', 'Car/Taxi'),
        ('metro', 'Metro'),
    ]
    DURATION_CHOICES = [
        ('short', '1-2 hours'),
        ('half_day', 'Half-day (4-6 hours)'),
        ('full_day', 'Full-day Trip'),
    ]
    
    visitor_type = forms.ChoiceField(choices=VISITOR_CHOICES, label="I am a:", widget=forms.Select(attrs={'class': 'form-control'}))
    interest = forms.ChoiceField(choices=INTEREST_CHOICES, label="I am interested in:", widget=forms.Select(attrs={'class': 'form-control'}))
    time = forms.ChoiceField(choices=TIME_CHOICES, label="Preferred time to visit:", widget=forms.Select(attrs={'class': 'form-control'}))
    budget = forms.ChoiceField(choices=BUDGET_CHOICES, label="Budget Range:", widget=forms.Select(attrs={'class': 'form-control'}))
    transport = forms.ChoiceField(choices=TRANSPORT_CHOICES, label="Mode of Transport:", widget=forms.Select(attrs={'class': 'form-control'}))
    duration = forms.ChoiceField(choices=DURATION_CHOICES, label="Duration of Visit:", widget=forms.Select(attrs={'class': 'form-control'}))

class LoginForms(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
    )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")


        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('password_confirm', "Passwords do not match.")
        return cleaned_data