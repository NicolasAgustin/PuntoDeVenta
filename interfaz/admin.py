from typing import Any
from django.contrib import admin

from interfaz.utils.enctyption_utils import encrypt_password
# Register your models here.
from interfaz.models import User

class UserAdmin(admin.ModelAdmin):

    def save_model(self, request: Any, obj: User, form: Any, change: Any) -> None:
        obj.password = encrypt_password(obj.password)
        return super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
