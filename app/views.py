from django.http import HttpResponse
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from app.models import App
from app.serializers import AppSerializer
from rest_framework.decorators import api_view

from .forms import FilterForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request)
    queryset = App.objects.all()
    # setup form
    my_form = FilterForm()
    # if request.method == "POST":
    #     my_form = FilterForm(request.POST)
        # if my_form.is_valid():
            # print(my_form.cleaned_data)
    name = request.POST.get('name')
    if name is not None:
        queryset = queryset.filter(name__icontains=name)
        # else:
        #     print(my_form.errors)
    apps_serializer = AppSerializer(queryset, many=True)
    context = {
        "object_list": apps_serializer.data,
        "form": my_form
    }
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", context)

@api_view(['GET', 'POST', 'DELETE'])
def list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
     if request.method == 'GET':
        apps =  App.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            apps = apps.filter(name__icontains=name)
        
        apps_serializer = AppSerializer(apps, many=True)
        return JsonResponse(apps_serializer.data, safe=False)
     elif request.method == 'POST':
        app_data = JSONParser().parse(request)
        app_serializer = AppSerializer(data=app_data)
        if app_serializer.is_valid():
            app_serializer.save()
            return JsonResponse(app_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
