from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import login, logout, authenticate
from rest_framework.permissions import IsAuthenticated
from dashboard.models import User
from dashboard.serializers import UserSerializer
from .token import get_tokens_for_user


@api_view(['POST'])
def sing_up_user(request):
    try:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            clone_password=password,
        )
        ser = UserSerializer(new)
        return Response(ser.data)
    except Exception as err:
        return Response({'message': str(err)})


@api_view(['POST'])
def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                login(request, usr)
                tokens = get_tokens_for_user(usr)
                status = 200
                data = {
                    'status': status,
                    'username': username,
                    'token': tokens,
                }
            else:
                status = 403
                message = "Invalid Password or Username!"
                data = {
                    'status': status,
                    'message': message,
                }
        except User.DoesNotExist:
            status = 404
            message = 'This User is not defined! '
            data = {
                'status': status,
                'message': message,
            }
        return Response(data)
    except Exception as err:
        return Response(f'{err}')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response({'data': 'sucses'})


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        try:
            ser = UserSerializer(user, data=request.data, partial=True)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        except:
            status = 404
            message = "Request failed"
            data = {
                'status': status,
                'message': message,
            }
    except:
        status = 404
        message = "User not found"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({'message': 'User deleted successfully'})
    except User.DoesNotExist:
        status = 404
        message = "User not found"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)


@api_view(['GET'])
def user_profile(request, pk):
    try:
        user = User.objects.get(pk=pk)
        ser = UserSerializer(user)
        return Response(ser.data)
    except User.DoesNotExist:
        status = 404
        message = "User not found"
        data = {
            'status': status,
            'message': message
        }
    return Response(data)

