from django.contrib import admin
from .models import AboutImages,AboutPage,OpenAndCloseHour,\
                    HotelLocationModel,HotelRoomImage,\
                    Rooms,MealModel,CustomerMassage
# Register your models here

admin.site.register(AboutImages)
admin.site.register(AboutPage)
admin.site.register(OpenAndCloseHour)
admin.site.register(HotelLocationModel)
admin.site.register(HotelRoomImage)
admin.site.register(Rooms)
admin.site.register(MealModel)
admin.site.register(CustomerMassage)