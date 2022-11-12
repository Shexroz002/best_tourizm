from rest_framework import serializers
from .models import TarixiyTurizmRasmlari,BizningGalereyamiz,BoglanishModel,\
                    BizBoglanishUchunModel,BizningMuzeylar,BizningRestoranlarniRasmlari,\
                    BizningRestoranlarhaqida,BizningSavdoMarkazlarniRasmlari,KorgazmalarRasmlari,\
                    TurizmTurlari,LogistikaTurlarimiz,BizningLogistikaRasmlari,Xodimlar,\
                    BizningSavdoMarkazlarhaqida,SafarTurizmRasmlari,YangiliklarModel,\
                    ExtremalTurizmModel,EtnikTurizmModel,EtnikTurizmRasmlari,YangiliklarRasmlari,\
                    ExtremalTurizmRasmlari
    


class TarixiyTurizmRasmlariSerializerUZB(serializers.ModelSerializer):

    class Meta:
        model = TarixiyTurizmRasmlari
        fields = ('id','name_uzb','image_file','date')


class TarixiyTurizmRasmlariSerializerRU(serializers.ModelSerializer):

    class Meta:
        model = TarixiyTurizmRasmlari
        fields = ('id','name_ru','image_file','date')


class TarixiyTurizmRasmlariSerializerENG(serializers.ModelSerializer):

    class Meta:
        model = TarixiyTurizmRasmlari
        fields = ('id','name_eng','image_file','date')

class SafarTurizmRasmlariSerializerUZB(serializers.ModelSerializer):

    class Meta:
        model = TarixiyTurizmRasmlari
        fields = ('id','name_uzb','title_uzb','image_file','date')

class SafarTurizmRasmlariSerializerRU(serializers.ModelSerializer):

    class Meta:
        model = TarixiyTurizmRasmlari
        fields = ('name_ru','title_ru','image_file','date')

class SafarTurizmRasmlariSerializerENG(serializers.ModelSerializer):

    class Meta:
        model = TarixiyTurizmRasmlari
        fields = ('id','name_eng','title_eng','image_file','date')

class BizningGalereyamizSerializer(serializers.ModelSerializer):

    class Meta:
        model = BizningGalereyamiz
        fields = "__all__"


class BoglanishModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoglanishModel
        fields = "__all__"
        extra_kwargs = {
            'name': {'required': True},
            'phone_number': {'required': True},
             'email': {'required': True},
            'message': {'required': True},
            
        }

    def create(self, validated_data):
        feed = BoglanishModel.objects.create(
            name = validated_data.get('name'),
            phone_number = validated_data.get('phone_number'),
            email = validated_data.get('email'),
            message = validated_data.get('message'),
        )
        feed.save()
        return feed


class BizBoglanishUchunModelSerializerUZB(serializers.ModelSerializer):

    class Meta:
        model = BizBoglanishUchunModel
        fields = ('id','location_uzb','phone_number','email','telegram_link','date')


class BizBoglanishUchunModelSerializerRU(serializers.ModelSerializer):

    class Meta:
        model = BizBoglanishUchunModel
        fields = ('id','location_ru','phone_number','email','telegram_link','date')


class BizBoglanishUchunModelSerializerENG(serializers.ModelSerializer):

    class Meta:
        model = BizBoglanishUchunModel
        fields = ('id','location_eng','phone_number','email','telegram_link','date')

class BizningMuzeylarSerializerUZB(serializers.ModelSerializer):

    class Meta:
        model = BizningMuzeylar
        fields = ('name_uzb','title_uzb','image_file','date')


class BizningMuzeylarSerializerRU(serializers.ModelSerializer):

    class Meta:
        model = BizningMuzeylar
        fields = ('id','name_ru','title_ru','image_file','date')


class BizningMuzeylarSerializerENG(serializers.ModelSerializer):

    class Meta:
        model = BizningMuzeylar
        fields = ('id','name_eng','title_eng','image_file','date')

class BizningRestoranlarniRasmlariSerializer(serializers.ModelSerializer):

    class Meta:
        model = BizningRestoranlarniRasmlari
        fields = "__all__"


class BizningRestoranlarhaqidaSerializerUZB(serializers.ModelSerializer):
    image_file=BizningRestoranlarniRasmlariSerializer(many=True)
    class Meta:
        model = BizningRestoranlarhaqida
        fields = ('id','title_uzb','image_file','date')


class BizningRestoranlarhaqidaSerializerRU(serializers.ModelSerializer):
    image_file=BizningRestoranlarniRasmlariSerializer(many=True)
    class Meta:
        model = BizningRestoranlarhaqida
        fields = ('id','title_ru','image_file','date')

class BizningRestoranlarhaqidaSerializerENG(serializers.ModelSerializer):
    image_file=BizningRestoranlarniRasmlariSerializer(many=True)
    class Meta:
        model = BizningRestoranlarhaqida
        fields = ('id','title_eng','image_file','date')


class BizningSavdoMarkazlarniRasmlariSerializer(serializers.ModelSerializer):

    class Meta:
        model = BizningSavdoMarkazlarniRasmlari
        fields = "__all__"


class BizningSavdoMarkazlarhaqidaSerializerUZB(serializers.ModelSerializer):
    image_file = BizningSavdoMarkazlarniRasmlariSerializer(many=True)
    class Meta:
        model = BizningSavdoMarkazlarhaqida
        fields = ('id','title_uzb','image_file','date')


class BizningSavdoMarkazlarhaqidaSerializerRU(serializers.ModelSerializer):
    image_file = BizningSavdoMarkazlarniRasmlariSerializer(many=True)

    class Meta:
        model = BizningSavdoMarkazlarhaqida
        fields = ('id','title_ru','image_file','date')

class BizningSavdoMarkazlarhaqidaSerializerENG(serializers.ModelSerializer):
    image_file = BizningSavdoMarkazlarniRasmlariSerializer(many=True)

    class Meta:
        model = BizningSavdoMarkazlarhaqida
        fields = ('id','title_eng','image_file','date')


class KorgazmalarRasmlariSerializer(serializers.ModelSerializer):

    class Meta:
        model = KorgazmalarRasmlari
        fields = "__all__"

class TurizmTurlariSerializerUZB(serializers.ModelSerializer):

    class Meta:
        model = TurizmTurlari
        fields = ('id','name_uzb','title_uzb','image_file','date')


class TurizmTurlariSerializerRU(serializers.ModelSerializer):

    class Meta:
        model = TurizmTurlari
        fields = ('id','name_ru','title_ru','image_file','date')


class TurizmTurlariSerializerENG(serializers.ModelSerializer):

    class Meta:
        model = TurizmTurlari
        fields = ('id','name_eng','title_eng','image_file','date')


class LogistikaTurlarimizSerializerUZB(serializers.ModelSerializer):

    class Meta:
        model = LogistikaTurlarimiz
        fields = ('name_uzb','title_uzb','image_file','date')


class LogistikaTurlarimizSerializerRU(serializers.ModelSerializer):

    class Meta:
        model = LogistikaTurlarimiz
        fields = ('id','name_ru','title_ru','image_file','date')


class LogistikaTurlarimizSerializerENG(serializers.ModelSerializer):

    class Meta:
        model = LogistikaTurlarimiz
        fields = ('id','name_eng','title_eng','image_file','date')


class BizningLogistikaRasmlariSerializer(serializers.ModelSerializer):

    class Meta:
        model = BizningLogistikaRasmlari
        fields = "__all__"

class XodimlarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Xodimlar
        fields = "__all__"

class YangiliklarRasmlariSerializer(serializers.ModelSerializer):

    class Meta:
        model = YangiliklarRasmlari
        fields = "__all__"

class YangiliklarModelSerializerUZB(serializers.ModelSerializer):
    image_file = YangiliklarRasmlariSerializer(many=True)
    class Meta:
        model = YangiliklarModel
        fields = ('id','name_uzb','title_uzb','image_file','date')


class YangiliklarModelSerializerRU(serializers.ModelSerializer):
    image_file = YangiliklarRasmlariSerializer(many=True)
    class Meta:
        model = YangiliklarModel
        fields = ('id','name_ru','title_ru','image_file','date')


class YangiliklarModelSerializerENG(serializers.ModelSerializer):
    image_file = YangiliklarRasmlariSerializer(many=True)
    class Meta:
        model = YangiliklarModel
        fields = ('id','name_eng','title_eng','image_file','date')

class EtnikTurizmRasmlariSerializer(serializers.ModelSerializer):

    class Meta:
        model = EtnikTurizmRasmlari
        fields = "__all__"

class EtnikTurizmModelSerializerUZB(serializers.ModelSerializer):
    image_file =EtnikTurizmRasmlariSerializer(many=True)
    class Meta:
        model = EtnikTurizmModel
        fields = ('id','name_uzb','title_uzb','image_file','date')


class EtnikTurizmModelSerializerRU(serializers.ModelSerializer):
    image_file =EtnikTurizmRasmlariSerializer(many=True)
    class Meta:
        model = EtnikTurizmModel
        fields = ('id','name_ru','title_ru','image_file','date')


class EtnikTurizmModelSerializerENG(serializers.ModelSerializer):
    image_file =EtnikTurizmRasmlariSerializer(many=True)
    class Meta:
        model = EtnikTurizmModel
        fields = ('id','name_eng','title_eng','image_file','date')

class ExtremalTurizmRasmlariSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtremalTurizmRasmlari
        fields = "__all__"

class ExtremalTurizmModelSerializerUZB(serializers.ModelSerializer):
    image_file = ExtremalTurizmRasmlariSerializer(many=True)
    class Meta:
        model = ExtremalTurizmModel
        fields = ('id','name_uzb','title_uzb','image_file','date')


class ExtremalTurizmModelSerializerRU(serializers.ModelSerializer):
    image_file = ExtremalTurizmRasmlariSerializer(many=True)
    class Meta:
        model = ExtremalTurizmModel
        fields = ('id','name_ru','title_ru','image_file','date')


class ExtremalTurizmModelSerializerENG(serializers.ModelSerializer):
    image_file = ExtremalTurizmRasmlariSerializer(many=True)
    class Meta:
        model = ExtremalTurizmModel
        fields = ('id','name_eng','title_eng','image_file','date')