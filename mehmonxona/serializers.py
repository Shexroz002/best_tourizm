from pyexpat import model
from rest_framework import serializers
from .models import HotelLocationModel,HotelRoomImage,OpenAndCloseHour,\
                   AboutImages, AboutPage,Rooms,MealModel,CustomerMassage



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

class CustomerMassageSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomerMassage
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True},
            'phone_nomer': {'required': True},
            'message': {'required': True},
           
        }
    def create(self, validated_data):
        photo = CustomerMassage.objects.create(
            name = validated_data['name'],
            email = validated_data['email'],
            phone_nomer = validated_data['phone_nomer'],
            message = validated_data['message'],
        )
        
        photo.save()
        return photo
