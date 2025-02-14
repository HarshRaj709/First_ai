from django import forms

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
