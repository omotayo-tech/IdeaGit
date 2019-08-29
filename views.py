from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User,Opinion, Comment
import bcrypt
import datetime


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        print('here')

        try:
            user = User.objects.get(email=request.POST['email'])

        except:
            messages.error(request, "E-mail or Password invalid.")
            print("redirecting after failed e-mail check")
            return redirect("/")
        if not bcrypt.checkpw(
                request.POST['loginpassword'].encode(), user.password.encode()):
            messages.error(request, "E-mail or Password invalid.")

            return redirect("/")

        print('HERE')

        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        request.session['email'] = user.email
        request.session['id'] = user.id
        print(user.password)
        return redirect("/homepage")
    else:
        return redirect("/")


def regisration_create(request):
    if request.method == 'POST':

        print("inside def registers")
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            print("inside else statement")
            hash = bcrypt.hashpw(request.POST['password'].encode(),
                                 bcrypt.gensalt())
            user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], description=request.POST["description"], city=request.POST["city"],
                                        website=request.POST["website"], phone_number=request.POST["phone_number"],  email=request.POST["email"], password=hash)
            messages.error(request, " You've been successfully registered")
            return redirect("/login")


def display_registration(request):
    return render(request, 'registration.html')
# Create your views here.
def home_page(request):
    context = {
        "all_opinions": Opinion.objects.all(),
        "access":  datetime.datetime.now()
    }
    return render(request, 'homepage.html', context)

def  point_of_view(request):
    if request.method == 'POST':
        errors = Opinion.objects.opinion_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/homepage')
        else:
            view = Opinion.objects.create(point_of_view=request.POST["point_of_view"], user=User.objects.get(
                email=request.session['email']))
    return redirect('/homepage')


def homepage_delete(request, id):
    delet = Opinion.objects.get(id=id)
    if(request.session['email'] == delet.user.email):
        delet.delete()
    return redirect('/homepage')



def homepage_info(request):
    context = {
        "user": User.objects.get(id=request.session['id'])
    }
    return render(request, 'homepage_info.html', context)
    
def homepage_added(request, id):
    grant = Opinion.objects.get(id=id)
    grant.added = True
    grant.added_at = datetime.datetime.now()
    grant.save()
    return redirect('/homepage')


def homepage_like(request, id):
    like = Opinion.objects.get(id=id)
    user =User.objects.get(id=request.session['id'])
    like.likes.add(user)
    return redirect('/homepage')


def logout(request):
    request.session['id'] = 0
    messages.error(request, "You have successfully logged out")
    return redirect('/')
   
def homepage_video(request):
    return render(request, 'homepage_videos.html')

def homepage_details(request, id):
    context ={
        "opinion":Opinion.objects.get(id=id)
    }
    return render(request, 'homepage_details.html', context)

def homepage_update(request, id):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            return redirect(f'/homepage/edit/{id}')

        else:
            s = User.objects.get(id=id)
            hash = bcrypt.hashpw(request.POST['password'].encode(),
                                 bcrypt.gensalt())
            s.first_name = request.POST['first_name']
            s.last_name = request.POST['last_name']
            s.desription = request.POST['description']
            s.city = request.POST['city']
            s.website = request.POST['website']
            s.phone_number = request.POST['phone_number']
            s.email = request.POST['email']
            s.passowrd = hash
            s.updated_at = datetime.datetime.now
            s.save()
    return redirect('/homepage/info')


def homepage_edit(request, id):
    user = User.objects.get(id=id)
    context = {
        "user": user
    }
    return render(request, 'homepage_edit.html', context)
