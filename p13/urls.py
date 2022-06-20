from django.contrib import admin
from django.urls import path, include

from oc_lettings_site import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    # path('profiles/', views.profiles_index, name='profiles_index'),
    # path('profiles/<str:username>/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
