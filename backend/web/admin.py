from django.contrib import admin

from web.models.user import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)


#让UserProfile模型接入 Django Admin 后台，并优化外键字段的操作体验，显示数据表