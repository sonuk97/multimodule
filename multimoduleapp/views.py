from django.shortcuts import render,redirect
from django.contrib import messages
from multimoduleapp.models import CustomUser,Usermember
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

@login_required(login_url='login1')
def admin_home(request):
    return render(request,'admin_home.html')

@login_required(login_url='login1')
def doctor_home(request):
    return render(request,'doctor_home.html')

@login_required(login_url='login1')
def patient_home(request):
    return render(request,'patient_home.html')

def patient_signup(request):
    return render(request,'patient_signup.html')
def doctor_signup(request):
    return render(request,'doctor_signup.html')
def login1(request):
    return render(request,'login.html')

def add_doctor(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        username = request.POST['uname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        age = request.POST['age']
        email = request.POST['email']
        cnumber = request.POST['number']
        image = request.FILES.get('file')
        user_type = request.POST['text']

        if password == cpassword:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('add_doctor')
            else:
                user = CustomUser.objects.create_user(
                    username=username, password=password, email=email, first_name=fname, last_name=lname, usertype=user_type)
                
                # Create Usermember instance and save it
                user1 = Usermember(age=age, number=cnumber, image=image, user=user)
                user1.save()
                
                return render(request, 'index.html')
        else:
            messages.info(request, "Password does not match")
            return redirect('add_doctor')

            
def add_patient(request):
    if request.method == 'POST':
       if request.method == 'POST':
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            username = request.POST.get('uname')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')
            age = request.POST.get('age')
            email = request.POST.get('email')
            cnumber = request.POST.get('number')
            image = request.FILES.get('file')
            user_type=request.POST['text']

            if password == cpassword:
                if CustomUser.objects.filter(username=username).exists():
                    messages.info(request, "Username already exists")
                    return redirect('add_patient')
                else:
                    user = CustomUser.objects.create_user(
                        username=username, password=password, email=email, first_name=fname, last_name=lname,usertype=user_type)
                    user.save()
                    user1 = Usermember(age=age, number=cnumber, image=image, user=user)
                    user1.save()
                    return render(request,'index.html')
            else:
                messages.info(request, "Password does not match")
                return redirect('add_patient')
       
def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('admin_home')
            elif user.usertype == '2':
                login(request, user)
                messages.info(request, f'WELCOME {username}')
                return redirect('doctor_home')
            else:
                login(request, user)
                messages.info(request, f'WELCOME {username}')
                return redirect('patient_home')
        else:
            messages.info(request, "Invalid Credentials")
            return render(request,'login.html')
    else:
        return render(request, 'index.html')
    
def log_out(request):
    
        auth.logout(request)
        return render(request,'index.html')
