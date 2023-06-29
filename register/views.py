from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def home(request):
    std=Student.objects.all()

    return render(request,"register/home.html", {"std":std})

def std_add(request):
    if request.method == "POST":
        print("Added")
        stds_roll = request.POST.get("std_roll")
        stds_name = request.POST.get("std_name")
        stds_address = request.POST.get("std_address")
        stds_course = request.POST.get("std_course")
        stds_email = request.POST.get("std_email")
        stds_phone = request.POST.get("std_phone")
        stds_semester = request.POST.get("std_semester")
        stds_language = request.POST.get("std_language")


        #create an object for models
        s=Student()
        s.roll = stds_roll
        s.name = stds_name
        s.address = stds_address
        s.course = stds_course
        s.email = stds_email
        s.phone = stds_phone
        s.semester = stds_semester
        s.language = stds_language


        s.save()
        return redirect("/register/home")

    return render(request,"register/add_std.html")

def delete_std(request,roll):
    s=Student.objects.get(pk=roll)
    s.delete()
    return redirect("/register/home")
def update_std(request,roll):
    std = Student.objects.get(pk=roll)

    return render(request,"register/update_std.html",{'std':std})
def do_update_std(request,roll):
    std_roll = request.POST.get("std_roll")
    std_name = request.POST.get("std_name")
    std_address = request.POST.get("std_address")
    std_course = request.POST.get("std_course")
    std_email = request.POST.get("std_email")
    std_phone = request.POST.get("std_phone")
    std_semester = request.POST.get("std_semester")
    std_language = request.POST.get("std_language")

    s = Student.objects.get(pk=roll)
    s.roll = std_roll
    s.name = std_name
    s.address = std_address
    s.course = std_course
    s.email = std_email
    s.phone = std_phone
    s.semester = std_semester
    s.language = std_language

    s.save()
    return redirect("/register/home")
