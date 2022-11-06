from django.shortcuts import render
from django.views import View
# Create your views here.


class TurPaketlar(View):
    def get(self,request):
        return render(request, 'index.html')


class Services(View):
    def get(self,request):
        return render(request, 'services.html')


class TypeTurism(View):
    def get(self,request):
        return render(request, 'typeTurism.html')


class Lagistika(View):
    def get(self,request):
        return render(request, 'logistics.html')


class TourismLaws(View):
    def get(self,request):
        return render(request, 'tourismLaws.html')

class News(View):
    def get(self,request):
        return render(request, 'news.html')


class NewsDetail(View):
    def get(self,request):
        return render(request, 'newsId.html')