from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp, Testimonial, Feedback
from .forms import FeedbackForm, EmpForm

# Create your views here.
def emp_home(request):
    return render(request, "emp/home.html", {})

def delete_emp(request, id):
    # print(id)
    emp = Emp.objects.get(id=id)
    emp.delete()
    # return redirect("/emp_mgmt/home/")
    return redirect("/emp_mgmt/emp-list/")

def update_emp(request, id):
    # print(id)
    emp = Emp.objects.get(id=id)
    return render(request, "emp/update_emp.html", {"emp":emp})
    
def do_update_emp(request, id):
    if request.method =="POST":
        name = request.POST.get('name')
        emp_id = request.POST.get('emp_id')
        emp_email = request.POST.get('emp_email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        working = request.POST.get('working')
        department = request.POST.get('department')
        e = Emp.objects.get(id=id)
        e.name=name
        e.emp_id=emp_id
        e.emp_email=emp_email
        e.phone=phone
        e.address=address
        e.department=department
        if working is None:
            e.working=False
        else:
            e.working=True
        
        e.save()
    return redirect("/emp_mgmt/emp-list/")


def emp_list(request):
    emps=Emp.objects.all()
    
    return render(request, "emp/emp_list.html", {"emps":emps})

def add_emp(request):
    data ={}
    if request.method == 'POST':
        # data fetch
        name = request.POST.get('name')
        emp_id = request.POST.get('emp_id')
        emp_email = request.POST.get('emp_email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        working = request.POST.get('working')
        department = request.POST.get('department')
        data = {"name":name, "emp_id":emp_id, "emp_email":emp_email, "phone":phone, "address":address, "working":working, "department":department}
        # create model object and set the data
        e=Emp()
        e.name=name
        e.emp_id=emp_id
        e.emp_email=emp_email
        e.phone=phone
        e.address=address
        e.department=department
        if working is None:
            e.working=False
        else:
            e.working=True
        # save the object
        e.save()
        return redirect("/emp_mgmt/emp-list/")
    # form = EmpForm()
    # form.save()
    return render(request, "emp/add_emp.html", data)

def testimonials(request):
    tet=Testimonial.objects.all()
    return render(request, "emp/testimonials.html",{"tet":tet})

def feedback(request):
    #  if this is a POST request we need to process the form data
    if request.method=='POST':
        # create a form instance and populate it with data from the request:
        form = FeedbackForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
             # Manually create and save the model instance
            obj = Feedback(
                name=data['name'],
                email=data['email'],
                feedback=data['feedback']
            )
            print(obj)
            #finally save the object in db
            obj.save()
            
            # print(form.cleaned_data['name'])
            # print(form.cleaned_data['email'])
            # print(form.cleaned_data['feedback'])

            print("data Saved Successfully!")
            # Optionally render a success page or redirect
            return render(request, "emp/feedback.html", {"form": FeedbackForm(), "success": True})
        else:
            return render(request, "emp/feedback.html", {"form":form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form=FeedbackForm()
        return render(request, "emp/feedback.html",{'form':form})