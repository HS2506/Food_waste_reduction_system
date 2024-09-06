from django.shortcuts import render
from .models import Donation

# View for listing donations
def donation_list(request):
    donations = Donation.objects.all()
    print("Donations:",donations)
    return render(request, 'donation_system/donation_list.html', {'donations': donations})

# View for adding a new donation
def add_donation(request):
    if request.method == 'POST':
        # Save the form data to the database
        pass  # Add form handling here
    return render(request, 'donation_system/add_donation.html')
