from django.contrib import admin
from django.urls import path, include
from customer_service import views  # Import app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Homepage with options
    path('submit-request/', views.submit_request, name='submit_request'),
    path('track-requests/', views.track_requests, name='track_requests'),

    # Include Django authentication views (login, logout)
    path('accounts/', include('django.contrib.auth.urls')),
]
