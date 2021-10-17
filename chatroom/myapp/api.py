from django.http import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import Userinfo

Host_url = "http://127.0.0.1:9000/upload/"


@api_view(['POST'])
def userLogin(res):

    username = res.POST['username']
    password = res.POST['password']
    print(username, password)
    user = User.objects.filter(username=username)
    if user:
        # print(user[0])
        isnotUser = check_password(password, user[0].password)
        print(isnotUser)
        if isnotUser:
            token = Token.objects.update_or_create(user=user[0])
            token = Token.objects.get(user=user[0]).key
            return Response(token)
        else:
            return Response('password error')
    else:
        return Response('user does not exist')


@api_view(['POST'])
def userInfo(res):
    token = res.POST['token']
    user = Token.objects.get(key=token).user
    userInfo = Userinfo.objects.get(belong=user)
    userInfo_data = {
        "nickName": userInfo.nickName,
        "photo": Host_url+str(userInfo.photo)
    }
    return Response(userInfo_data)
