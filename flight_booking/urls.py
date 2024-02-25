from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/users/login/')),  # Redirect to the login page of the users app
    path('users/', include('users.urls')),
    path('flights/', include('flights.urls')),
    # Add other app URLs here
]
