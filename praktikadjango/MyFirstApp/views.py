from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class TestView(View):
    def get(self, request):
        persons = Person.objects.all()
        print(persons.last().pets.all())
        pets = Pet.objects.all()
        return render(request, 'test.html', {'persons': persons, 'pets': pets})