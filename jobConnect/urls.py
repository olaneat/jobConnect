
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('account/', include('register.urls', namespace='register')),
    path('admin/', admin.site.urls),
    path('profile/', include('details.urls', namespace="detail")),
    path('rest-auth/password/reset/', include('rest_auth.urls')),
    path('project/', include('project.urls', namespace="project")),
    path('account/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
