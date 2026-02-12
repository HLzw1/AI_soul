from web.views.user.account.get_user_info import GetUserInfoView
from web.views.user.account.login import LoginView
from django.urls import path, re_path
from web.views.index import index
from web.views.user.account.logout import LogoutView
from web.views.user.account.register import RegisterView
from web.views.user.account.refresh_token import RefreshTokenView
urlpatterns = [
    path('api/user/account/login/', LoginView.as_view(), name='login'),
    path('api/user/account/logout/', LogoutView.as_view(), name='logout'),
    path('api/user/account/register/', RegisterView.as_view(), name='register'),
    path('api/user/account/refresh_token/', RefreshTokenView.as_view(), name='refresh_token'),
    path('api/user/account/get_user_info/', GetUserInfoView.as_view(), name='get_user_info'),
    path('', index),

    # 正则表达式排除所有后端路由并返回前端路由index.html前端路由（有router)
    #eg: friend下路由匹配到最后一项返回index.html（前端view),view里有RouterView返回对应组件
    re_path(r'^(?!media/|static/|assets/).*$', index)

]