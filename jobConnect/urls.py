
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
	path('account/', include('register.urls', namespace='register')),
    path('admin/', admin.site.urls),
    path('profile/', include('details.urls', namespace="detail")),
    re_path(r'^/rest_auth/password/reset/', include('rest_auth.urls')),
    path('/password/reset/confirm/', include('rest_auth.urls')),
    path('/password/change/', include('rest_auth.urls')),
    path('project/', include('project.urls', namespace="project")),
    path('account/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
