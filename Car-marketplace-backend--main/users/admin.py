from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from users.models import CustomUser,Permission,Role,Features


class UserAdmin(UserAdmin):
  form = UserChangeForm
  fieldsets = (
      (None, {'fields': ('email', 'password', )}),
      (_('Personal info'), {'fields': ('first_name', 'last_name')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': ('full_name', 'phone','location','role')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  list_display = ['email', 'first_name', 'last_name', 'is_staff', "phone",'location']
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email', )


admin.site.register(CustomUser,UserAdmin)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(Features)

