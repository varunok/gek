from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register your models here.
from users.models import User


class CustomUserAdmin(UserAdmin):
    list_display = [
        'email',
        'group',
        'first_name',
        'last_name',

    ]

    list_filter = ('group',)

    fieldsets = (
                (None, {'fields': ('email', 'password')}),
                ('Personal info', {
                 'fields': (
                     'avatar',
                     'first_name',
                     'last_name',
                     'middle_name',
                     'phone',
                     'skype',
                 )}),
                ('Professional info', {
                    'fields': (
                        'address',
                        'specialization',
                        'extra',
                        'about_self',
                        'video',
                    )
                }),
                ('Permissions', {'fields': ('is_staff', 'group')}),
                ('Important dates', {'fields': ('last_login', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'group',
                'password1',
                'password2'
            )}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)