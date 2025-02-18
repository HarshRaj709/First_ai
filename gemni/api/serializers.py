from rest_framework import serializers

class FormSerializer(serializers.Serializer):
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


    visitor_type = serializers.ChoiceField(choices = VISITOR_CHOICES)
    interest = serializers.ChoiceField(choices = INTEREST_CHOICES)
    time = serializers.ChoiceField(choices = TIME_CHOICES)
    budget = serializers.ChoiceField(choices = BUDGET_CHOICES)
    transport = serializers.ChoiceField(choices = TRANSPORT_CHOICES)
    duration = serializers.ChoiceField(choices = DURATION_CHOICES)
