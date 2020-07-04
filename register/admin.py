from .forms import CustomUserForm, CustomChangeUserForm
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class CustomAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields':('email', 'password')}),
        (_('person_info'), {'fields':('last_name', 'first_name')}),
        (_('permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                'groups', 'user_permissions')}),
        (_('important dates'), {'fields':('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes':('wide', ),
            'fields': ('email', 'password1', 'password2', 'is_active', 'groups', 'is_staff', 'is_superuser' )
        }),

    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', )
    ordering = ('email',)
