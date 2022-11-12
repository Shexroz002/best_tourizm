from email.policy import default
from django.db import models

# Create your models here.
class TarixiyTurizmRasmlari(models.Model):
    name_uzb = models.CharField(max_length = 90,default='',verbose_name = "O'zbekcha nomi")
    name_ru = models.CharField(max_length = 90 ,default='',verbose_name = "Ruscha nomi")
    name_eng = models.CharField(max_length = 90,default='',verbose_name = "Inglizcha nomi")
    title_uzb = models.CharField(max_length = 90,default='',verbose_name = "O'zbekcha haqida malimot")
    title_ru = models.CharField(max_length = 90 ,default='',verbose_name = "Ruscha haqida malimot")
    title_eng = models.CharField(max_length = 90,default='',verbose_name = "Inglizcha haqida malimot")
    image_file  = models.ImageField(upload_to = 'tarixiy_turizm_rasmlari/',null=False,blank = False,verbose_name = "Rasm faylni kirting")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_uzb




class BizningGalereyamiz(models.Model):
    name = models.CharField(max_length = 90,default='',verbose_name = "Rasm nomi")
    image_file  = models.ImageField(upload_to = 'bizning_galeryamiz/',null=False,blank = False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BoglanishModel(models.Model):
    name = models.CharField(max_length = 60,default='',verbose_name = "Ismi",null=False,blank=False)
    phone_number = models.CharField(max_length = 12,default='',verbose_name = "Telefon nomeri",null=False,blank=False)
    email = models.EmailField(max_length = 60,default='',verbose_name = "Email",null=False,blank=False)
    message = models.CharField(max_length = 12,default='',verbose_name = "Qoldirilgan xabar",null=False,blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class BizBoglanishUchunModel(models.Model):
    location_uzb = models.CharField(max_length = 60,default='',verbose_name = "Manzil(Uzbek)")
    location_ru = models.CharField(max_length = 60,default='',verbose_name = "Manzil(Ruscha)")
    location_eng = models.CharField(max_length = 60,default='',verbose_name = "Manzil(English)")
    phone_number = models.CharField(max_length = 12,default='',verbose_name = "Telefon nomeri")
    email = models.EmailField(max_length = 60,default='',verbose_name = "Email")
    telegram_link = models.CharField(max_length = 12,default='',verbose_name = "Telegram link")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.location_uzb

class BizningMuzeylar(models.Model):
    name_uzb = models.CharField(max_length = 90,default='',verbose_name = "O'zbekcha nomi")
    name_ru = models.CharField(max_length = 90 ,default='',verbose_name = "Ruscha nomi")
    name_eng = models.CharField(max_length = 90,default='',verbose_name = "Inglizcha nomi")
    title_uzb = models.TextField(max_length = 2500,default='',verbose_name = "haqida malimot kirting(Uzb)")
    title_ru = models.TextField(max_length = 2500 ,default='',verbose_name = "haqida malimot kirting(Rus)")
    title_eng = models.TextField(max_length = 2500,default='',verbose_name = "haqida malimot kirting(Eng)")
    image_file  = models.ImageField(upload_to = 'bizning_muzeyimiz/',null=False,blank = False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_uzb


class BizningRestoranlarniRasmlari(models.Model):
    name = models.CharField(max_length = 90 ,default='images',verbose_name = "Rasm nomi")
    image_file  = models.ImageField(upload_to = 'bizning_restaranlari_rasmlari/',null=False,blank = False)

    def __str__(self):
        return self.name

class BizningRestoranlarhaqida(models.Model):
    title_uzb = models.TextField(max_length = 2500,default='',verbose_name = "Restoranlar haqida malimot kirting(Uzb)")
    title_ru = models.TextField(max_length = 2500 ,default='',verbose_name = "Restoranlar haqida malimot kirting(Rus)")
    title_eng = models.TextField(max_length = 2500,default='',verbose_name = "Restoranlar haqida malimot kirting(Eng)")
    image_file  = models.ManyToManyField(BizningRestoranlarniRasmlari,related_name='imagefilerestaurant',verbose_name = "Restoranlar haqida rasm kirting")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title_uzb


class BizningSavdoMarkazlarniRasmlari(models.Model):
    name = models.CharField(max_length = 90 ,default='images',verbose_name = "Rasm nomi")
    image_file  = models.ImageField(upload_to = 'bizning_savdo_markazlar_rasmlari/',null=False,blank = False)

    def __str__(self):
        return self.name

class BizningSavdoMarkazlarhaqida(models.Model):
    title_uzb = models.TextField(max_length = 2500,default='',verbose_name = "Savdo Markaz haqida malimot kirting(Uzb)")
    title_ru = models.TextField(max_length = 2500 ,default='',verbose_name = "Savdo Markaz haqida malimot kirting(Rus)")
    title_eng = models.TextField(max_length = 2500,default='',verbose_name = "Savdo Markaz haqida malimot kirting(Eng)")
    image_file  = models.ManyToManyField(BizningSavdoMarkazlarniRasmlari,related_name='imagefile',verbose_name = "Savdo Markaz haqida rasm kirting")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title_uzb

class KorgazmalarRasmlari(models.Model):
    name = models.CharField(max_length = 90 ,default='images',verbose_name = "Rasm nomi")
    image_file  = models.ImageField(upload_to = 'bizning_korgazmalar_rasmlari/',null=False,blank = False)
    
    def __str__(self):
        return self.name

class TurizmTurlari(models.Model):
    name_uzb = models.CharField(max_length = 90,default='',verbose_name = "Turizm turi O'zbekcha nomi")
    name_ru = models.CharField(max_length = 90 ,default='',verbose_name = "Turizm turi Ruscha nomi")
    name_eng = models.CharField(max_length = 90,default='',verbose_name = "Turizm turi Inglizcha nomi")
    title_uzb = models.TextField(max_length = 2500,default='',verbose_name = "Turizm turi haqida malimot kirting(Uzb)")
    title_ru = models.TextField(max_length = 2500 ,default='',verbose_name = "Turizm turi haqida malimot kirting(Rus)")
    title_eng = models.TextField(max_length = 2500,default='',verbose_name = "Turizm turi haqida malimot kirting(Eng)")
    image_file  = models.ImageField(upload_to = 'turizm_turlari_rasmlar/',null=False,blank = False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_uzb

class LogistikaTurlarimiz(models.Model):
    name_uzb = models.CharField(max_length = 90,default='',verbose_name = "Logistika Turi O'zbekcha nomi")
    name_ru = models.CharField(max_length = 90 ,default='',verbose_name = "Logistika Turi Ruscha nomi")
    name_eng = models.CharField(max_length = 90,default='',verbose_name = "Logistika Turi Inglizcha nomi")
    title_uzb = models.TextField(max_length = 2500,default='',verbose_name = "Logistika Turi haqida malimot kirting(Uzb)")
    title_ru = models.TextField(max_length = 2500 ,default='',verbose_name = "Logistika Turi haqida malimot kirting(Rus)")
    title_eng = models.TextField(max_length = 2500,default='',verbose_name = "Logistika Turii haqida malimot kirting(Eng)")
    image_file  = models.ImageField(upload_to = 'lagistika_turi_rasmlari/',null=False,blank = False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_uzb

class BizningLogistikaRasmlari(models.Model):
    name = models.CharField(max_length = 90 ,default='images',verbose_name = "Rasm nomi")
    image_file  = models.ImageField(upload_to = 'bizning_logistika_rasmlari/',null=False,blank = False)

    def __str__(self):
        return self.name


class Xodimlar(models.Model):
    full_name = models.CharField(max_length = 190,default='',verbose_name = "F.I.SH")
    degree = models.CharField(max_length = 190,default='',verbose_name = "Lavozim")
    phone_number = models.CharField(max_length = 190,default='',verbose_name = "Telefon raqami")
    email = models.EmailField(max_length = 190,default='',verbose_name = "Elektron pochta manzil")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class YangiliklarRasmlari(models.Model):
    name = models.CharField(max_length = 90 ,default='images',verbose_name = "Rasm nomi")
    image_file  = models.ImageField(upload_to = 'yangilkilar_images/',null=False,blank = False,verbose_name = "Rasm filesni")

    def __str__(self):
        return self.name


class YangiliklarModel(models.Model):
    name_uzb = models.CharField(max_length = 900,default='',verbose_name = "Yangilik nomi (uzbek)")
    name_ru = models.CharField(max_length = 900 ,default='',verbose_name = "Yangilik nomi (ruscha)")
    name_eng = models.CharField(max_length = 900,default='',verbose_name = "Yangilik nomi (english)")
    title_uzb = models.TextField(max_length = 5500,default='',verbose_name = "Yangilik haqida (uzbek)")
    title_ru = models.TextField(max_length = 5500 ,default='',verbose_name = "Yangilik haqida (ruscha)")
    title_eng = models.TextField(max_length = 5500,default='',verbose_name = "Yangilik haqida (english)")
    image_file  = models.ManyToManyField(YangiliklarRasmlari,related_name='imagefile',verbose_name = "Yangilikar haqida  rasm kirting")
    date = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.name_uzb

class ExtremalTurizmRasmlari(models.Model):
    name = models.CharField(max_length = 90 ,default='images',verbose_name = "Rasm nomi")
    image_file  = models.ImageField(upload_to = 'exteremal_turizm_rasmlari/',null=False,blank = False,verbose_name = "Rasm filesni")

    def __str__(self):
        return self.name


class ExtremalTurizmModel(models.Model):
    name_uzb = models.CharField(max_length = 90,default='',verbose_name = "Extremal turizm O'zbekcha nomi")
    name_ru = models.CharField(max_length = 90 ,default='',verbose_name = "Extremal turizm Ruscha nomi")
    name_eng = models.CharField(max_length = 90,default='',verbose_name = "Extremal turizm Inglizcha nomi")
    title_uzb = models.TextField(max_length = 2500,default='',verbose_name = "Extremal turizm haqida malimot kirting(Uzb)")
    title_ru = models.TextField(max_length = 2500 ,default='',verbose_name = "Extremal turizm haqida malimot kirting(Rus)")
    title_eng = models.TextField(max_length = 2500,default='',verbose_name = "Extremal turizm haqida malimot kirting(Eng)")
    image_file  = models.ManyToManyField(ExtremalTurizmRasmlari,related_name='imagefile',verbose_name = "exteremal turizm rasmni kirting")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_uzb

class EtnikTurizmRasmlari(models.Model):
    name = models.CharField(max_length = 90 ,default='images',verbose_name = "Rasm nomi")
    image_file  = models.ImageField(upload_to = 'etnik_turizm_rasmlari/',null=False,blank = False,verbose_name = "Rasm filesni")

    def __str__(self):
        return self.name


class EtnikTurizmModel(models.Model):
    name_uzb = models.CharField(max_length = 90,default='',verbose_name = "Etnik turizm O'zbekcha nomi")
    name_ru = models.CharField(max_length = 90 ,default='',verbose_name = "Etnik turizm Ruscha nomi")
    name_eng = models.CharField(max_length = 90,default='',verbose_name = "Etnik turizm Inglizcha nomi")
    title_uzb = models.TextField(max_length = 2500,default='',verbose_name = "Etnik turizm haqida malimot kirting(Uzb)")
    title_ru = models.TextField(max_length = 2500 ,default='',verbose_name = "Etnik turizm haqida malimot kirting(Rus)")
    title_eng = models.TextField(max_length = 2500,default='',verbose_name = "Etnik turizm haqida malimot kirting(Eng)")
    image_file  = models.ManyToManyField(EtnikTurizmRasmlari,related_name='Etnik',verbose_name = "Etnik turizm rasmni kirting")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_uzb

class SafarTurizmRasmlari(models.Model):
    name = models.CharField(max_length = 90 ,default='images',verbose_name = "Rasm nomi")
    image_file  = models.ImageField(upload_to = 'etnik_turizm_rasmlari/',null=False,blank = False,verbose_name = "Rasm filesni")

    def __str__(self):
        return self.name


class SafarTurizmModel(models.Model):
    name_uzb = models.CharField(max_length = 90,default='',verbose_name = "Etnik turizm O'zbekcha nomi")
    name_ru = models.CharField(max_length = 90 ,default='',verbose_name = "Etnik turizm Ruscha nomi")
    name_eng = models.CharField(max_length = 90,default='',verbose_name = "Etnik turizm Inglizcha nomi")
    title_uzb = models.TextField(max_length = 2500,default='',verbose_name = "Etnik turizm haqida malimot kirting(Uzb)")
    title_ru = models.TextField(max_length = 2500 ,default='',verbose_name = "Etnik turizm haqida malimot kirting(Rus)")
    title_eng = models.TextField(max_length = 2500,default='',verbose_name = "Etnik turizm haqida malimot kirting(Eng)")
    image_file  = models.ManyToManyField(SafarTurizmRasmlari,related_name='Etnik',verbose_name = "Etnik turizm rasmni kirting")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_uzb