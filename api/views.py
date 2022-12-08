from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import TarixiyTurizmRasmlari,BizningGalereyamiz,BoglanishModel,\
                    BizBoglanishUchunModel,BizningMuzeylar,BizningRestoranlarniRasmlari,\
                    BizningRestoranlarhaqida,BizningSavdoMarkazlarniRasmlari,KorgazmalarRasmlari,\
                    TurizmTurlari,LogistikaTurlarimiz,BizningLogistikaRasmlari,Xodimlar,\
                    BizningSavdoMarkazlarhaqida,SafarTurizmRasmlari,YangiliklarModel,\
                    EtnikTurizmModel,ExtremalTurizmModel,SafarTurizmModel,HammaSahifadaChiqadiganRasmlarModel
from .serializers import TarixiyTurizmRasmlariSerializerUZB,TarixiyTurizmRasmlariSerializerRU,TarixiyTurizmRasmlariSerializerENG,\
                        BizningGalereyamizSerializer,BoglanishModelSerializer,\
                        BizBoglanishUchunModelSerializerUZB,BizBoglanishUchunModelSerializerRU,BizBoglanishUchunModelSerializerENG,\
                        BizningMuzeylarSerializerUZB,BizningMuzeylarSerializerRU,BizningMuzeylarSerializerENG,\
                        BizningRestoranlarniRasmlariSerializer,\
                        BizningRestoranlarhaqidaSerializerUZB,BizningRestoranlarhaqidaSerializerRU,BizningRestoranlarhaqidaSerializerENG,\
                        BizningSavdoMarkazlarniRasmlariSerializer,\
                        BizningSavdoMarkazlarhaqidaSerializerUZB,BizningSavdoMarkazlarhaqidaSerializerRU,BizningSavdoMarkazlarhaqidaSerializerENG,\
                        KorgazmalarRasmlariSerializer,\
                        TurizmTurlariSerializerUZB,TurizmTurlariSerializerRU,TurizmTurlariSerializerENG,\
                        LogistikaTurlarimizSerializerUZB,LogistikaTurlarimizSerializerENG,LogistikaTurlarimizSerializerRU,\
                        BizningLogistikaRasmlariSerializer, XodimlarSerializer,SafarTurizmModelSerializerUZB,\
                        SafarTurizmModelSerializerRU,SafarTurizmModelSerializerENG,YangiliklarModelSerializerENG,\
                        YangiliklarModelSerializerRU,YangiliklarModelSerializerUZB,EtnikTurizmModelSerializerENG,\
                        EtnikTurizmModelSerializerRU,EtnikTurizmModelSerializerUZB,ExtremalTurizmModelSerializerENG,\
                        ExtremalTurizmModelSerializerRU,ExtremalTurizmModelSerializerUZB,HammaSahifadaChiqadiganRasmlarModelSerializerUZB,\
                        HammaSahifadaChiqadiganRasmlarModelSerializerRU,HammaSahifadaChiqadiganRasmlarModelSerializerENG       
from rest_framework import status
from rest_framework import response
from rest_framework import views

class TarixiyTurizmRasmlariAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        tarixy_turizm = TarixiyTurizmRasmlari.objects.all()
        if language == 'uzb':
            return response.Response(TarixiyTurizmRasmlariSerializerUZB(tarixy_turizm,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(TarixiyTurizmRasmlariSerializerRU(tarixy_turizm,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(TarixiyTurizmRasmlariSerializerENG(tarixy_turizm,many=True).data,status=status.HTTP_200_OK)
        return response.Response(TarixiyTurizmRasmlariSerializerUZB(tarixy_turizm,many=True).data,status=status.HTTP_200_OK)

class SafarTurizmModelAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        safar_turizm = SafarTurizmModel.objects.all()
        if language == 'uzb':
            return response.Response(SafarTurizmModelSerializerUZB(safar_turizm,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(SafarTurizmModelSerializerRU(safar_turizm,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(SafarTurizmModelSerializerENG(safar_turizm,many=True).data,status=status.HTTP_200_OK)
        return response.Response(SafarTurizmModelSerializerUZB(safar_turizm,many=True).data,status=status.HTTP_200_OK)





class BizningGalereyamizAPIViews(views.APIView):
    def get(self,request):
        galarya= BizningGalereyamiz.objects.all()
        return response.Response(BizningGalereyamizSerializer(galarya,many=True).data,status=status.HTTP_200_OK)


class BoglanishModelAPIViews(views.APIView):
    def get(self,request):
        boglanish= BoglanishModel.objects.all()
        return response.Response(BoglanishModelSerializer(boglanish,many=True).data,status=status.HTTP_200_OK)
    def post(self,request):
        boglanish_serializer = BoglanishModelSerializer(data=request.data)
        if boglanish_serializer.is_valid():
            boglanish_serializer.save()
            return response.Response(boglanish_serializer.data,status=status.HTTP_201_CREATED)
        else:
            return response.Response({'error':boglanish_serializer.errors},status=status.HTTP_201_CREATED)

class BizBoglanishUchunModeliAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        boglansh = BizBoglanishUchunModel.objects.all()
        if language == 'uzb':
            return response.Response(BizBoglanishUchunModelSerializerUZB(boglansh,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(BizBoglanishUchunModelSerializerRU(boglansh,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(BizBoglanishUchunModelSerializerENG(boglansh,many=True).data,status=status.HTTP_200_OK)
        return response.Response(BizBoglanishUchunModelSerializerUZB(boglansh,many=True).data,status=status.HTTP_200_OK)


class BizningMuzeylarAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        muzey = BizningMuzeylar.objects.all()
        if language == 'uzb':
            return response.Response(BizningMuzeylarSerializerUZB(muzey,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(BizningMuzeylarSerializerRU(muzey,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(BizningMuzeylarSerializerENG(muzey,many=True).data,status=status.HTTP_200_OK)
        return response.Response(BizningMuzeylarSerializerUZB(muzey,many=True).data,status=status.HTTP_200_OK)


class BizningRestoranlarniRasmlariAPIViews(views.APIView):
    def get(self,request):
        restaran= BizningRestoranlarniRasmlari.objects.all()
        return response.Response(BizningRestoranlarniRasmlariSerializer(restaran,many=True).data,status=status.HTTP_200_OK)


class BizningRestoranlarhaqidaAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        restarant_haqida = BizningRestoranlarhaqida.objects.all()
        if language == 'uzb':
            return response.Response(BizningRestoranlarhaqidaSerializerUZB(restarant_haqida,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(BizningRestoranlarhaqidaSerializerRU(restarant_haqida,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(BizningRestoranlarhaqidaSerializerENG(restarant_haqida,many=True).data,status=status.HTTP_200_OK)
        return response.Response(BizningRestoranlarhaqidaSerializerUZB(restarant_haqida,many=True).data,status=status.HTTP_200_OK)


class BizningSavdoMarkazlarniRasmlariAPIViews(views.APIView):
    def get(self,request):
        savdo_rasmlari= BizningSavdoMarkazlarniRasmlari.objects.all()
        return response.Response(BizningSavdoMarkazlarniRasmlariSerializer(savdo_rasmlari,many=True).data,status=status.HTTP_200_OK)


class BizningSavdoMarkazlarhaqidaAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        savdo_markazlar = BizningSavdoMarkazlarhaqida.objects.all()
        if language == 'uzb':
            return response.Response(BizningSavdoMarkazlarhaqidaSerializerUZB(savdo_markazlar,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(BizningSavdoMarkazlarhaqidaSerializerRU(savdo_markazlar,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(BizningSavdoMarkazlarhaqidaSerializerENG(savdo_markazlar,many=True).data,status=status.HTTP_200_OK)
        return response.Response(BizningSavdoMarkazlarhaqidaSerializerUZB(savdo_markazlar,many=True).data,status=status.HTTP_200_OK)


class KorgazmalarRasmlariAPIViews(views.APIView):
    def get(self,request):
        korgazmalar= KorgazmalarRasmlari.objects.all()
        return response.Response(KorgazmalarRasmlariSerializer(korgazmalar,many=True).data,status=status.HTTP_200_OK)



class TurizmTurlariAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        turizm_turlari = TurizmTurlari.objects.all()
        if language == 'uzb':
            return response.Response(TurizmTurlariSerializerUZB(turizm_turlari,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(TurizmTurlariSerializerRU(turizm_turlari,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(TurizmTurlariSerializerENG(turizm_turlari,many=True).data,status=status.HTTP_200_OK)
        return response.Response(TurizmTurlariSerializerUZB(turizm_turlari,many=True).data,status=status.HTTP_200_OK)


class LogistikaTurlarimizAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        logistika_turlari = LogistikaTurlarimiz.objects.all()
        if language == 'uzb':
            return response.Response(LogistikaTurlarimizSerializerUZB(logistika_turlari,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(LogistikaTurlarimizSerializerRU(logistika_turlari,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(LogistikaTurlarimizSerializerENG(logistika_turlari,many=True).data,status=status.HTTP_200_OK)
        return response.Response(LogistikaTurlarimizSerializerUZB(logistika_turlari,many=True).data,status=status.HTTP_200_OK)

class BizningLogistikaRasmlariAPIViews(views.APIView):
    def get(self,request):
        logistika_rasmlari= BizningLogistikaRasmlari.objects.all()
        return response.Response(BizningLogistikaRasmlariSerializer(logistika_rasmlari,many=True).data,status=status.HTTP_200_OK)


class XodimlarAPIViews(views.APIView):
    def get(self,request):
        xodimlar= Xodimlar.objects.all()
        return response.Response(XodimlarSerializer(xodimlar,many=True).data,status=status.HTTP_200_OK)

class YangiliklarModelAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        yangiliklar = YangiliklarModel.objects.all()
        if language == 'uzb':
            return response.Response(YangiliklarModelSerializerUZB(yangiliklar,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(YangiliklarModelSerializerRU(yangiliklar,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(YangiliklarModelSerializerENG(yangiliklar,many=True).data,status=status.HTTP_200_OK)
        return response.Response(YangiliklarModelSerializerUZB(yangiliklar,many=True).data,status=status.HTTP_200_OK)

class YangiliklarDetailModelAPIViews(views.APIView):
    def get(self,request,id):
        language  = request.GET.get('language', None)
        yangiliklar = get_object_or_404(YangiliklarModel,id=id)
        if language == 'uzb':
            return response.Response(YangiliklarModelSerializerUZB(yangiliklar).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(YangiliklarModelSerializerRU(yangiliklar).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(YangiliklarModelSerializerENG(yangiliklar).data,status=status.HTTP_200_OK)
        return response.Response(YangiliklarModelSerializerUZB(yangiliklar).data,status=status.HTTP_200_OK)


class EtnikTurizmModelAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        etnik = EtnikTurizmModel.objects.all()
        if language == 'uzb':
            return response.Response(EtnikTurizmModelSerializerUZB(etnik,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(EtnikTurizmModelSerializerRU(etnik,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(EtnikTurizmModelSerializerENG(etnik,many=True).data,status=status.HTTP_200_OK)
        return response.Response(EtnikTurizmModelSerializerUZB(etnik,many=True).data,status=status.HTTP_200_OK)

class ExtremalTurizmModelAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        etnik = ExtremalTurizmModel.objects.all()
        if language == 'uzb':
            return response.Response(ExtremalTurizmModelSerializerUZB(etnik,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(ExtremalTurizmModelSerializerRU(etnik,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(ExtremalTurizmModelSerializerENG(etnik,many=True).data,status=status.HTTP_200_OK)
        return response.Response(ExtremalTurizmModelSerializerUZB(etnik,many=True).data,status=status.HTTP_200_OK)

class HammaSahifadaChiqadiganRasmlarModelAPIViews(views.APIView):
    def get(self,request):
        language  = request.GET.get('language', None)
        all_data = HammaSahifadaChiqadiganRasmlarModel.objects.all()
        if language == 'uzb':
            return response.Response(HammaSahifadaChiqadiganRasmlarModelSerializerUZB(all_data,many=True).data,status=status.HTTP_200_OK)
        if language == 'rus':
            return response.Response(HammaSahifadaChiqadiganRasmlarModelSerializerRU(all_data,many=True).data,status=status.HTTP_200_OK)
        if language == 'eng':
            return response.Response(HammaSahifadaChiqadiganRasmlarModelSerializerENG(all_data,many=True).data,status=status.HTTP_200_OK)
        return response.Response(HammaSahifadaChiqadiganRasmlarModelSerializerUZB(all_data,many=True).data,status=status.HTTP_200_OK)