from django.urls import path
from .views import  AboutPageAPIViews,HotelLocationModelAPIViews,RoomsAPIViews,\
                    MealModelAPIViews,OpenAndCloseHourAPIViews,HotelRoomImageAPIViews

urlpatterns = [
    path('about/page',AboutPageAPIViews.as_view()),
    path('location/',HotelLocationModelAPIViews.as_view()),
    path('rooms/',RoomsAPIViews.as_view()),
    path('meals/',MealModelAPIViews.as_view()),
    path('open/and/close',OpenAndCloseHourAPIViews.as_view()),
    path('rooms/images',HotelRoomImageAPIViews.as_view()),
]
                    
