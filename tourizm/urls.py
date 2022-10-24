from django.urls import path
from .views import TurPaketlar,Services,TypeTurism,Lagistika,TourismLaws

urlpatterns = [
    path('', TurPaketlar.as_view()),
    path('services/', Services.as_view()),
    path('typeturizm/', TypeTurism.as_view()),
    path('logistika/', Lagistika.as_view()),
    path('law/', TourismLaws.as_view()),
    # path('api/', include('api.urls')),
    # path('', include('tourizm.urls')),
]
