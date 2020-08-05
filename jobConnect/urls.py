
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
	path('account/', include('register.urls', namespace='register')),
    path('admin/', admin.site.urls),
    path('profile/', include('details.urls', namespace="detail")),
    path('auth', include('rest_framework.urls')),
    re_path(r'^/rest_auth/password/reset/', include('rest_auth.urls')),
    path('/password/reset/confirm/', include('rest_auth.urls')),
    path('/password/change/', include('rest_auth.urls')),
    path('project/', include('project.urls', namespace="project")),
    path('account/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
