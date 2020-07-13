
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('account/', include('register.urls', namespace='register')),
    path('admin/', admin.site.urls),
    path('profile/', include('details.urls', namespace="detail")),
    path('project/', include('project.urls', namespace="project")),
]
