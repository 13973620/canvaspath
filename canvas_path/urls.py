from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/login/', views.login, name='login'), # index redirect to login
    path('users/', include('users.urls')),  # new
    path('admin/', admin.site.urls),

]
