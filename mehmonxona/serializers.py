from pyexpat import model
from rest_framework import serializers
from .models import HotelLocationModel,HotelRoomImage,OpenAndCloseHour,\
                   AboutImages, AboutPage,Rooms,MealModel



class AboutImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutImages
        fields = '__all__'


class AboutPageSerializers(serializers.ModelSerializer):
    photo_files = AboutImagesSerializers(read_only=True,many=True)
    class Meta:
        model = AboutPage
        fields = '__all__'


class RoomsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class MealModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = MealModel
        fields = '__all__'


class HotelRoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelRoomImage
        fields = '__all__'

class OpenAndCloseHourSerializers(serializers.ModelSerializer):
    class Meta:
        model = OpenAndCloseHour
        fields = '__all__'

class HotelLocationModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelLocationModel
        fields = '__all__'