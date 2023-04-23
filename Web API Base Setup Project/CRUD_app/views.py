from django.shortcuts import render
from django.db.backends import postgresql
from .models import *
from datetime import datetime
from django.http import JsonResponse


# Create your views here.


# Request a simple HTML page to add data of patient
def home(request):

    return render(request, 'base.html')


def update_page(request, id):
     data = patient.objects.filter(id=id).get()
     print(data.id)
     return render(request, 'update.html', {'data': data})

def update(request, id):
    
    print('I am in update Function')
    
    name = request.POST.get('patient_name', "Umer")
    act = request.POST.get('patient_activity', "Walk")
    age = request.POST.get('patient_age', 25)

    print(name)
    patient.objects.filter(id=id).update(name =name, activty = act, age = age , time = datetime.now().strftime("%H:%M:%S"))

    print('patient updated')
    return render(request, 'base.html')

# POST request for adding data
def add(request):
    # print(request.method)
    # if request.method == "POST":


    name = request.POST['patient_name']
    act = request.POST['patient_activity']
    age = request.POST['patient_age']

    # print(name)

    # patient = patient(name= name, activity= act, age= age, time= datetime.now().strftime("%H:%M:%S"))

    p = patient(name= name , 
                    activty = act, 
                    age = age, 
                    time = datetime.now().strftime("%H:%M:%S"))

    p.save()
    print('patient created in database')
    

    return render(request, 'base.html')


# Get All Patients List in JSON format
def get_patients(request):

    data = list(patient.objects.values())  # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)


# Get Patient by its id
def get_by_id(request , id):
    return JsonResponse(list(patient.objects.filter(id= id ).values()), safe=False)


# Get Patient through any attribute of patient
# Example link like this
# localhost/get_by_att/id/1
def get_by_att(request, att, val):
    print(att)
    return JsonResponse(list(patient.objects.filter( **{att: val} ).values()), safe=False)


def update_patient(request,id, data):
    patient.objects.filter(id=id).update(data)


def delete_by_id(request, id):
    patient.objects.filter(id = id).delete()
    return JsonResponse(list(patient.objects.values()), safe=False)