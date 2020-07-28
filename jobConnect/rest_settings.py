
REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework_simplejwt.authentication.JWTAuthentication',
   ),
   'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated'
   ),

   'DEFAULT_PAGINATION_CLASS': 'project.paginations.CustomizedPagination',
   'PAGE_SIZE': 10,
}
