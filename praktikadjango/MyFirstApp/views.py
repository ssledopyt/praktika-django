from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class TestView(View):
    def get(self, request):
        return render(request, 'test.html',
                      {
                          'persons': Person.objects.have_pets(False),
                          'pets': Pet.objects.have_friends(True),
                      }
                      )


class TestPlayView(View):
    def get(self, request):
        return render(request, 'testplay.html',
                      {
                          'houses': Home.objects.all()
                      }
                      )
