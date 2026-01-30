from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from web.models.user import UserProfile

#实现接口，后面将结合js/http/api，在前端页面调用这个接口，对应前端页面LoginIndex

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:                                                #用户输入
            username = request.data['username'].strip()
            password = request.data['password'].strip()
            if not username or not password:
                return Response({
                    'result': '用户名或密码不能为空'
                })
            user = authenticate(username=username, password=password)   #认证用户密码
            if user:
                user_profile = UserProfile.objects.get(user = user)
                refresh = RefreshToken.for_user(user)           #生成jwt
                response = Response({                       #保存access
                    'result': 'success',
                    'access': str(refresh.access_token),
                    'user_id': user.id,
                    'refresh': str(refresh),
                    'username': user.username,
                    'photo': user_profile.photo.url,
                    'profile': user_profile.profile,
                })
                response.set_cookie(                    #设置cookie
                    key='refresh_token',
                    value=str(refresh),
                    httponly=True,
                    samesite='Lax',
                    secure=True,
                    max_age=86400 * 7,
                )
                return response
            return Response({
                'result': '用户名或密码错误'
            })
        except:
            return Response({
                'result': '系统异常，稍后重试'
            })