# myapp/models.py
from django.db import models

class Emergency(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Person(models.Model):

    HAIR_COLOR_CHOICES = [
        ('Brown', 'Brown'),
        ('Blonde', 'Blonde'),
        ('Black', 'Black'),
        ('Red', 'Red'),
        ('Other', 'Other'),
    ]

    EYE_COLOR_CHOICES = [
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        ('Brown', 'Brown'),
        ('Hazel', 'Hazel'),
        ('Other', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    hair_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    distinctive_features = models.TextField()
    daybirth = models.DateField(blank=True, null=True)
    document_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Finding(models.Model):
    emergency = models.ForeignKey(Emergency, on_delete=models.CASCADE)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    found_location = models.CharField(max_length=255)
    found_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name} found in {self.emergency.name}"
