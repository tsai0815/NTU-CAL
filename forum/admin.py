from django.contrib import admin
from .models import Question, Solution
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    # 定義列表顯示的欄位
    list_display = ('username', 'email', 'password')
    # 定義可點擊進行詳細查看的欄位
    list_display_links = ('username', 'email')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(Question)
admin.site.register(Solution)

