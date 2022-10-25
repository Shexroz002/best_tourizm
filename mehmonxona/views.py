from django.shortcuts import render
from rest_framework import views 
from .models import AboutPage,Rooms,MealModel,OpenAndCloseHour,HotelRoomImage,HotelLocationModel
from .serializers import AboutPageSerializers,RoomsSerializers,\
                    MealModelSerializers,OpenAndCloseHourSerializers,\
                        HotelRoomImageSerializers,HotelLocationModelSerializers

from rest_framework import response
from rest_framework import status
# Create your views here.


class AboutPageAPIViews(views.APIView):
    def get(self,request):
        about_page = AboutPage.objects.all().order_by("-added_at")
        return response.Response(AboutPageSerializers(about_page,many=True).data,status=status.HTTP_200_OK)


class RoomsAPIViews(views.APIView):
    def get(self,request):
        rooms = Rooms.objects.all().order_by("-added_at")
        return response.Response(RoomsSerializers(rooms,many=True).data,status=status.HTTP_200_OK)



class MealModelAPIViews(views.APIView):
    def get(self,request):
        meals = MealModel.objects.all().order_by("-added_at")
        return response.Response(MealModelSerializers(meals,many=True).data,status=status.HTTP_200_OK)


class OpenAndCloseHourAPIViews(views.APIView):
    def get(self,request):
        open_and_close = OpenAndCloseHour.objects.all().order_by("-added_at")
        return response.Response(OpenAndCloseHourSerializers(open_and_close,many=True).data,status=status.HTTP_200_OK)


class HotelRoomImageAPIViews(views.APIView):
    def get(self,request):
        room_image = HotelRoomImage.objects.all().order_by("-added_at")
        return response.Response(HotelRoomImageSerializers(room_image,many=True).data,status=status.HTTP_200_OK)


class HotelLocationModelAPIViews(views.APIView):
    def get(self,request):
        hotel_location = HotelLocationModel.objects.all().order_by("-added_at")
        return response.Response(HotelLocationModelSerializers(hotel_location,many=True).data,status=status.HTTP_200_OK)
