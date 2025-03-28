from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'customer_service/home.html')  # Renders a template with options

@login_required  # Ensure user is logged in
def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user  # Assign logged-in user
            service_request.save()
            return redirect('track_requests')  # Redirect after submission
        else:
            print("Form errors:", form.errors)  # Debugging
    else:
        form = ServiceRequestForm()
    
    return render(request, 'customer_service/submit_request.html', {'form': form})
@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'customer_service/track_requests.html', {'requests': requests})
