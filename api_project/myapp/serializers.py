# myapp/serializers.py
from rest_framework import serializers
from django.utils.text import slugify, strip_tags
from .models import Person, Emergency, Finding

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    # Sanitization
    def validate_first_name(self, value):
        # Use slugify to standardize capitalization
        return slugify(value)

    # Sanitization
    def validate_last_name(self, value):
        # Use slugify to standardize capitalization
        return slugify(value)
    
    # Validation
    def validate_age(self, value):
        if value < 0 or value > 150:
            raise serializers.ValidationError("Age must be between 0 and 150.")
        return value
    
    # Validation
    def validate_hair_color(self, value):
        if value not in self.HAIR_COLOR_CHOICES:
            raise serializers.ValidationError(
                f"Invalid hair color. Choose from: {', '.join(self.HAIR_COLOR_CHOICES)}."
            )
        return value

    # Validation
    def validate_eye_color(self, value):
        if value not in self.EYE_COLOR_CHOICES:
            raise serializers.ValidationError(
                f"Invalid eye color. Choose from: {', '.join(self.EYE_COLOR_CHOICES)}."
            )
        return value

    # Sanitization & Security
    def validate_distinctive_features(self, value):
        # Use strip_tags to remove HTML tags
        return strip_tags(value)


class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = '__all__'

class FindingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finding
        fields = '__all__'
