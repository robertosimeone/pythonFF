from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField
from .models import (
    Statistic,
    User,
    Movie,
    Profile,
    Comment,
    Order,
)

admin.site.register(Movie)

class UserAdminSelf(UserAdmin):
    list_display = (
        'email', 'username', 'password', 'token', 'streak_number', 'is_admin', 'is_superuser', 'is_active', 'is_staff',
        'profile_image', 'date_joined', 'last_login')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserAdminSelf)


class UserChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.username


class StatisticsAdmin(admin.ModelAdmin):
    model = Statistic
    formfield_overrides = {
        models.ForeignKey: {'form_class': UserChoiceField},
    }
class ProfileChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.username


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    formfield_overrides = {
        models.ForeignKey: {'form_class': ProfileChoiceField},
    }
class OrderChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.username


class OrderAdmin(admin.ModelAdmin):
    model = Order
    formfield_overrides = {
        models.ForeignKey: {'form_class': OrderChoiceField},
    }
admin.site.register(Order,OrderAdmin)
admin.site.register(Comment)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Statistic, StatisticsAdmin)
# admin.site.register(Comment)
