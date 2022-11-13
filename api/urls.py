from django.urls import path
from .views import TarixiyTurizmRasmlariAPIViews,BizningGalereyamizAPIViews,BoglanishModelAPIViews,\
                   BizBoglanishUchunModeliAPIViews,BizningMuzeylarAPIViews,BizningRestoranlarniRasmlariAPIViews,\
                   BizningRestoranlarhaqidaAPIViews,BizningSavdoMarkazlarniRasmlariAPIViews,BizningSavdoMarkazlarhaqidaAPIViews,\
                   KorgazmalarRasmlariAPIViews,TurizmTurlariAPIViews,LogistikaTurlarimizAPIViews,\
                   BizningLogistikaRasmlariAPIViews,SafarTurizmModelAPIViews,YangiliklarModelAPIViews,\
                   YangiliklarDetailModelAPIViews,EtnikTurizmModelAPIViews,ExtremalTurizmModelAPIViews

urlpatterns = [
    path('tarixiy/turizm/rasmlar',TarixiyTurizmRasmlariAPIViews.as_view()),
    path('safar/turizm/rasmlar',SafarTurizmModelAPIViews.as_view()),
    path('bizning/galeryamiz',BizningGalereyamizAPIViews.as_view()),
    path('biz/bilan/boglanish',BoglanishModelAPIViews.as_view()),
    path('client/bilan/boglanish',BizBoglanishUchunModeliAPIViews.as_view()),
    path('bizning/muzeylar',BizningMuzeylarAPIViews.as_view()),
    path('restaran/rasmlar',BizningRestoranlarniRasmlariAPIViews.as_view()),
    path('restaran/haqida',BizningRestoranlarhaqidaAPIViews.as_view()),
    path('savdo/markaz/rasmlari',BizningSavdoMarkazlarniRasmlariAPIViews.as_view()),
    path('savdo/markaz/haqida',BizningSavdoMarkazlarhaqidaAPIViews.as_view()),
    path('korgazmalar',KorgazmalarRasmlariAPIViews.as_view()),
    path('turizm/turlari',TurizmTurlariAPIViews.as_view()),
    path('logistika/turlari',LogistikaTurlarimizAPIViews.as_view()),
    path('logistika/rasmlari',BizningLogistikaRasmlariAPIViews.as_view()),
    path('yangiliklar',YangiliklarModelAPIViews.as_view()),
    path('yangiliklar/<int:id>',YangiliklarDetailModelAPIViews.as_view()),
    path('etnik/turizm',EtnikTurizmModelAPIViews.as_view()),
    path('extremal/turizm',ExtremalTurizmModelAPIViews.as_view()),
]
