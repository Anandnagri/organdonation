from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from odms.models import Feedback, Donor


# Create your views here.

@login_required
def HomePage(request):
    return render(request, 'index.html', {})


def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pass')

        new_user = User.objects.create_user(name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')

    return render(request, 'register.html', {})


def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error, user does not exist')

    return render(request, 'login.html', {})


def logoutuser(request):
    logout(request)
    return redirect('login-page')


def donor(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        fathername = request.POST['fathername']
        mothername = request.POST['mothername']
        gender = request.POST['gender']
        organ = request.POST['organ']
        date_of_birth = request.POST['date_of_birth']
        bloodgroup = request.POST['bloodgroup']
        aadharnumber = request.POST['aadharnumber']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        emergencynumber = request.POST['emergencynumber']
        add = request.POST['add']
        ins = Donor(firstname=firstname, lastname=lastname, fathername=fathername, mothername=mothername, gender=gender, organ=organ, date_of_birth=date_of_birth, bloodgroup=bloodgroup, aadharnumber=aadharnumber, email=email, phonenumber=phonenumber, emergencynumber=emergencynumber, add=add)
        ins.save()
    return render(request, 'donor.html', {})

def reciever(request):
    donordata = Donor.objects.all()
    if request.method=="GET":
        se=request.GET.get('searchname')
        if se!=None:
            donordata = Donor.objects.filter(organ__icontains=se)
    context = {'reciver': donordata}
    return render(request, 'reciver.html', context)


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def feedback(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        feedback = request.POST['feedback']
        ins = Feedback(name=name, email=email, phonenumber=phonenumber, feedback=feedback)
        ins.save()
        print("ok")
    return render(request, 'feedback2.html', {})


def test(request):
    return render(request, 'test.html', {})

def faq(request):
    return render(request, 'faq.html', {})
