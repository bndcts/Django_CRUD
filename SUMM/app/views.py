from django.http import HttpResponse
from .models import Translation, User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, TranslationSerializer
from rest_framework import serializers
from rest_framework import status


def home(request):
    return HttpResponse("Coding challenge for SUMM")

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_Users': '/users/all',
        'Add_user': '/users/add',
        'Update_user': '/update/pk',
        'Delete_user': '/users/pk/delete',
        'all_Translations': '/translations',
        'Add_translation': '/translations/add',
        'Update_translation': '/translations/update/pk',
        'Delete_translation': '/translations/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_user(request):
    user = UserSerializer(data=request.data)
    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data does already exist.')
    
    if user.is_valid():
        user.save()
        return Response(user.data)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
def view_users(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        Users = User.objects.filter(**request.query_param.dict())
    else:
        Users = User.objects.all()
  
    # if there is something in Users else raise error
    if Users:
        data = UserSerializer(Users, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_users(request, pk):
    user = User.objects.get(pk=pk)
    data = UserSerializer(instance=user, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_users(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def add_translation(request):
    translation = TranslationSerializer(data=request.data)
    if Translation.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data does already exist.')
    
    if translation.is_valid():
        translation.save()
        return Response(translation.data)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET'])
def view_translations(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        Translations = Translation.objects.filter(**request.query_param.dict())
    else:
        Translations = Translation.objects.all()
  
    # if there is something in Translations else raise error
    if Translations:
        data = TranslationSerializer(Translations, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_translations(request, pk):
    translation = Translation.objects.get(pk=pk)
    data = TranslationSerializer(instance=translation, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_translations(request, pk):
    translation = get_object_or_404(Translation, pk=pk)
    translation.delete()
    return Response(status=status.HTTP_202_ACCEPTED)