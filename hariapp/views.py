from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    # return HttpResponse("<p>This is index page</p>")
    msg=''
    isActive = True
    if request.method == 'POST':
        # msg = request.POST['msg']
        msg = request.POST.get('msg')
        print(msg)
        if msg is None: isActive=False
        else: isActive = True
    date = datetime.datetime.now()
    
    name = "Harinarayan"
    list_of_programs = [
        "WAP to sum of 1 to 10",
        "WAP to print even and odd number",
        "WAP to check prime number",
        "WAP to print prime number from 1 to 100"
    ]
    student ={
        "name":"Harinarayan Kumar",
        "college":"XYZ",
        "roll_no": 12456,
        "city":"New Delhi"
    }
    return render(request, "home.html", {"date":date,"isActive":isActive, "name":name, "list_of_programs":list_of_programs, "student_data":student, "msg":msg })

def contact(request):
    # return HttpResponse("<p>This is index page</p>")
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")

def about(request):
    return render(request, "about.html")
