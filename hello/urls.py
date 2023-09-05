from django.contrib import admin
from django.urls import path, include


# username and password for admin is admin.

admin.site.site_header = "Natural's Ice Cream"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Natural's"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls')),
    
]
