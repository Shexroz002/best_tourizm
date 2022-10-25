from email.policy import default
from django.db import models

# Create your models here.

class AboutImages(models.Model):
    photo_name = models.CharField(max_length = 30,default='',verbose_name = "About pagega chiqadigan rasm nomi")
    photo_file = models.ImageField(upload_to = 'about_image/',null=False,blank=False,verbose_name = "About pagega chiqadigan rasm files")
    added_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.photo_name


class AboutPage(models.Model):
    title = models.CharField(max_length = 10000,default='',blank=False,verbose_name = "About Pageda chiqadigan ma'limot")
    photo_files = models.ManyToManyField(AboutImages,related_name='photo_files',blank=True,verbose_name = "About Pagega chiqadigan rasmlarni tanlang")
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class OpenAndCloseHour(models.Model):
    open_hour = models.TimeField(verbose_name = "Mehmonhonani ochilish vaqti")
    close_hour = models.TimeField(verbose_name = "Mehmonhonani yopilish vaqti")
    opan_close_day = models.CharField(max_length = 70,default='Monday to Friday',verbose_name = "Mehmonhonani ishlash kunlari")
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opan_close_day

class Rooms(models.Model):
    room_name = models.CharField(max_length = 250,verbose_name = "Xonani nomi")
    room_title = models.CharField(max_length = 1000,verbose_name = "Xonani haqida malimot")
    room_price = models.FloatField(verbose_name = "Xonani narxi")
    room_file = models.ImageField(upload_to = 'room_image/',null=False,blank=False,verbose_name = "Xonani rasmi")
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name


class MealChoice(models.IntegerChoices):
    HOTDISH = 0, 'HOTDISH'
    DESSERT = 1, 'DESSERT'
    
class MealModel(models.Model):
    meal_name = models.CharField(max_length = 100,verbose_name = "Nomi")
    meal_title = models.CharField(max_length = 100,verbose_name = "haqida malimot")
    meal_price = models.FloatField(verbose_name = "Narxi")
    catagorya = models.IntegerField(choices=MealChoice.choices, default=MealChoice.HOTDISH,verbose_name = "Turi")
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.meal_name


class HotelRoomImage(models.Model):
    hotel_room_image = models.ImageField(upload_to = 'hotel_room_image/',null=False,blank=False,verbose_name = "Mehmon xona rasm")
    hotel_room_name = models.CharField(max_length = 100,verbose_name = "Mehmonxona nomi")
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel_room_name

class CustomerMassage(models.Model):
    name = models.CharField(max_length = 150,default='',verbose_name = "Foydalanuvchi nomi")
    email = models.EmailField(max_length = 150,default='',verbose_name = "Foydalanuvchi email")
    phone_nomer = models.IntegerField(default=0,null=False,blank=True,verbose_name = "Foydalanuvchi  telefon nomeri")
    message = models.CharField(max_length = 1000,default = '',verbose_name = "Foydalanuvchi yuborgan xabar")
    added_at = models.DateTimeField(auto_now_add=True)

class HotelLocationModel(models.Model):
    hotel_name =  models.CharField(max_length = 150,default='',verbose_name = "Nomi")
    hotel_location =  models.CharField(max_length = 150,default='',verbose_name = "Joylashgan Hudud")
    hotel_phone =  models.IntegerField(default=0,null=False,blank=True,verbose_name = "Telefon nomeri")
    hotel_email =  models.EmailField(default=0,null=False,blank=True,verbose_name = "email")
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel_name
