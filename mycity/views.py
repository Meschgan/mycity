from django.shortcuts import render 
from mycity.models import Citizen


def index(request):  
    citizens = Citizen.objects.order_by('id').all()
    context = {'citizens': citizens}
    return render(request, 'mycity/index.html', context)

