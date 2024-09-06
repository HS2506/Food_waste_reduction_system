from django.db import models
from django.contrib.auth.models import User

# Donation Model
class Donation(models.Model):
    FOOD_TYPES = [
        ('Cooked', 'Cooked Food'),
        ('Uncooked', 'Uncooked Ingredients'),
        ('Packaged', 'Packaged Food'),
        ('Non-edible', 'Non-edible Food'),
    ]
    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    food_type = models.CharField(max_length=20, choices=FOOD_TYPES)
    quantity = models.PositiveIntegerField()
    pickup_time = models.DateTimeField()
    requires_cold_storage = models.BooleanField(default=False)
    needs_decomposition = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.food_type} ({self.quantity} kg) by {self.donor}"

# Cold Storage Truck Model
class ColdStorageTruck(models.Model):
    truck_id = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    current_location = models.CharField(max_length=255)
    availability_status = models.BooleanField(default=True)
    temperature_conditions = models.CharField(max_length=50)

    def __str__(self):
        return f"Truck {self.truck_id} ({self.company_name})"

# Decomposition Guide Model
class DecompositionGuide(models.Model):
    food_type = models.CharField(max_length=20)
    decomposition_method = models.TextField()
    partner_company = models.CharField(max_length=100)
    estimated_time = models.DurationField()
    eco_friendly_rating = models.PositiveIntegerField()

    def __str__(self):
        return f"Guide for {self.food_type}"
