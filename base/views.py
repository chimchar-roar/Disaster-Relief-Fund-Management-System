# myapp/views.py
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from .forms import CitizenUserCreationForm, StaffUserCreationForm
from .models import CitizenUser,CitizenDetails,StaffUser,Survey,Transfer
from django.contrib import messages

def home(request):
    return render(request,'home.html',{})

def citizen_register(request):
    if request.method == 'POST':
        form = CitizenUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('citizen_login')  # Redirect to the home page or another URL
    else:
        form = CitizenUserCreationForm()
    return render(request, 'registration/citizen_register.html', {'form': form})

def staff_register(request):
    if request.method == 'POST':
        form = StaffUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_login')  # Redirect to the home pag or another URL
        else:
            print('error')
    else:
        form = StaffUserCreationForm()
    return render(request, 'registration/staff_register.html', {'form': form})

def citizen_login(request):
    msg=''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Credentials are valid, proceed to login
            login(request, user)
            # Redirect to a success page or perform other actions
            return redirect('home-view')
        else:
            # Credentials are not valid, handle authentication failure
            msg='Invalid username or password'
    
    return render(request,'login/citizenLogin.html',{'msg':msg})

def staff_login(request):
    msg=''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Credentials are valid, proceed to login
            login(request, user)
            # Redirect to a success page or perform other actions
            return redirect('staff-home')
        else:
            # Credentials are not valid, handle authentication failure
            msg='Invalid staff id or password'

    
    return render(request,'login/staffLogin.html',{'msg':msg})

@login_required(login_url="/login/citizen/")
def citizen_home(request):
    user=request.user.username
    ob=CitizenUser.objects.filter(username=user)
    return redirect('home-view')

@login_required(login_url="/login/citizen/")
def citizen_applicationform(request):
    user=request.user.username
    ob=CitizenDetails.objects.filter(username=user)
    ob2=CitizenUser.objects.filter(username=user)
    print(ob2)
    if ob.exists():
        return redirect('citizen-details-display')
    if request.method=='POST':
        instance=CitizenDetails()
        instance.username=user
        instance.name=ob2[0].name
        instance.house_no=request.POST['house_no']
        instance.house_name=request.POST['house_name']
        instance.address=request.POST['address']
        instance.village_code=request.POST['village_code']
        instance.aadhar_no=request.POST['aadhar_no']
        instance.ration_no=request.POST['ration_no']
        instance.account_no=request.POST['account_no']
        instance.ifsc=request.POST['ifsc']
        instance.description=request.POST['description']
        instance.save()
        return redirect("home-view")
  
    return render(request,'allforms/applicationform_fill.html',{})


@login_required(login_url="login/citizen/")
def citizen_details_display(request):
    user=request.user.username
    ob=CitizenDetails.objects.filter(username=user)
    return render(request,'allforms/applicationform_display.html',{'instance':ob[0]})

@login_required(login_url="login/citizen/")
def citizen_application_status(request):
    user=request.user.username
    ob=CitizenDetails.objects.filter(username=user)
    if not ob:
        msg='Please fill application form'
    elif ob[0].survey_result:
        msg='Application Accepted'
    else:
        msg='Application under scrutiny'
    return render(request,'allforms/citizen_status.html',{'msg':msg})

@login_required(login_url="login/staff/")
def staff_citizens(request):
    user=request.user.username
    staffob=StaffUser.objects.filter(username=user)
    print(staffob)
    objs=CitizenDetails.objects.filter(village_code=staffob[0].village_code)
    url='/staff/home/'
    return render(request,'homepage/citizen.html',{'cid':staffob[0].pk,'objs':objs,'url':url,'i':1})

def logoutUser(request):
    logout(request)
    return redirect('home-view')

@login_required(login_url="login/staff/")
def displaytostaff(request,username):
    ob = CitizenDetails.objects.filter(username=username)
    ob2=Survey.objects.filter(username=username)
    view=False
    if not ob2.exists():
        print('username =',ob[0])
        user=ob[0]
        instance=Survey()
        instance.username=user
        instance.name=ob[0].name
        instance.house_no=ob[0].house_no
        instance.house_name=ob[0].house_name
        instance.address=ob[0].address
        instance.estimated_loss=0
        instance.save()
    url1='/staff/home/survey/'
    url2='/staff/home/survey_display/'
    if ob2:
        if ob2[0].survey_desc:
            view=True
    return render(request,'allforms/applicationform_display.html',{'instance':ob[0],'url1':url1,'url2':url2,'view':view,'username':username,})

def staff_home(request):
    return render(request,'homepage/staffhome.html')

def staff_transactions(request):
    return render(request,'homepage/transferdetes.html')

def about(request):
    return render(request,'homepage/about.html')

def surveyform_fill(request,username):
    instance=Survey.objects.get(username=username)
    if request.method=='POST':
        instance.survey_desc=request.POST.get('survey_desc')
        instance.estimated_loss=request.POST.get('estimated_loss')
        # instance[0].survey_desc=request.POST['survey_desc']
        # instance[0].estimated_loss=request.POST['estimated_loss']
        instance.save()
        ob=CitizenDetails.objects.get(username=username)
        ob.survey_result=True
        ob.save()
        print(instance.name)
        print(instance.survey_desc)
        return HttpResponseRedirect('/staff/home/citizens/')
    return render(request,'allforms/surveyform_fill.html',{'instance':instance})

def display_surveyform(request,username):
    instance=Survey.objects.filter(username=username)
    return render(request,'allforms/surveyform_display.html',{'instance':instance[0]})

