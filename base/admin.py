from django.contrib import admin
from .models import (
Statistic,
User,
Movie,
MyAccountManager,

)
admin.site.register(User)
admin.site.register(Statistic)
admin.site.register(Movie)

# Register your models here.
