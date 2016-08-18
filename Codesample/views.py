from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.core.context_processors import csrf
from models import UserModel, Fotos
from forms import LoginForm, FotosForm
import json


def profile(request):
    if request.user.is_authenticated():
        use=UserModel.objects.get(id=request.user.id)
    else:
        return HttpResponse('Invalid User')
    return render(request, 'profile.html',{'use':use})


# def show(request, id):
#     post = get_object_or_404(CodePost, id=id)
#     return render(request, 'post.html', {'post': post})


def edit(request):
    print '1'
    if request.user.is_authenticated():
        print '2'
        if request.method=='POST':
            print '3'
            if request.POST.get('operation')=='edit' and request.POST.get('id'):
                print '4'
                print request.POST.get('id')
                foto=Fotos.objects.get(id=request.POST.get('id'))
                foto.name=request.POST.get('name')
                foto.save()
                print 'EDITED'
                return HttpResponse('EDITED')
            elif request.POST.get('operation')=='delete' and request.POST.get('id'):
                print '5'
                Fotos.objects.get(id=request.POST.get('id')).delete()
                print 'DELETED'
                return HttpResponse('OK')
            else:
                print '6'
                return HttpResponse('<div class="alert-danger">SOMETHING WENT WRONG PLEASE TRY AGAIN!!!</div>')
        else:
            print '7'
            return HttpResponse('<div class="alert-danger">DONT MESS WITH ME!!!</div>')
    return HttpResponse('<div class="alert-danger">GO AND LOGIN FIRST!!!</div>')



@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')


def login_user(request):
    form = LoginForm()
    print '1'

    if request.user.is_authenticated():
        print '2'
        return HttpResponseRedirect('/')

    if request.method == "POST":
        print '3'
        print request.POST.get("email")
        print request.POST.get("password")
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        print 'Printing ', user
        if user != None:
            print '4'
            if user.is_active:
                print '5'
                login(request, user)
                response_data = {'message': 'Loggedin'}
                return HttpResponseRedirect('/')
            else:
                print '6'
                response_data = {'message': "Your account has been disabled!"}
        else:
            print '7'
            response_data = {'message': 'The username and password are incorrect.'}
            return render(request, 'login.html', response_data)
    else:
        print '8'
        return render(request, 'login.html', {'form': form, 'message': 'Please Login First!'})
    print '9'
    return render(request, 'login.html', {'form': form})


#
# def postit(request):
#     print 'postitt'
#     if request.method=='POST' and request.FILES:
#         if request.user.is_authenticated():
#             userr=UserModel.objects.get(email=request.user.email)
#             Fotos.objects.create( name=request.POST.get('name'),
#             datee=datetime.now(),
#             author=userr,
#             foto=request.FILES['foto'],
#             likes=0,
#             shares=0,
#             )
#             print 'Saved'
#         else:
#             return HttpResponse('login')
#     else:
#         HttpResponse('<div class="alert-danger">SOMETHING WENT WRONG PLEASE TRY AGAIN!!!</div>')

def register(request):
    print 'okay'
    if request.method == 'POST':
        print 'okay2'
        form = RegistrationForm(request.POST)
        print 'Print Form : ', form
        if form:
            print 'okay3'
            user = UserModel.objects.create_user(
                username=request.POST.get('username'),
                password=request.POST.get('password'),
                email=request.POST.get('email'),
            )
            print 'the user : ', user
            user.first_name = request.POST.get('firstname')
            user.last_name = request.POST.get('lastname')
            user.city_town = request.POST.get('citytown')
            user.mobile = request.POST.get('mobile')
            user.dp = request.FILES['dp']
            print 'user :', user
            user.save()
            return HttpResponseRedirect("/login")
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def publish(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            if request.POST and request.FILES:
                userr = UserModel.objects.get(email=request.user.email)
                Fotos.objects.create(name=request.POST.get('name'),
                                     date=datetime.now(),
                                     author=userr,
                                     foto=request.FILES['foto'],
                                     likes=0,
                                     comments=0,
                                     shares=0,
                                     )
                print 'Saved'
                return HttpResponseRedirect('/')
            else:
                aform = FotosForm()
                return render(request, 'publish.html', {'form': aform})
        else:
            HttpResponse('login')
    else:
        HttpResponse('<div class="alert-danger">SOMETHING WENT WRONG PLEASE TRY AGAIN!!!</div>')


def allposts(request):
    if request.user.is_authenticated():
        posts = Fotos.objects.filter().order_by('-date')
        print posts
        return HttpResponse(render(request, 'posts.html', {'posts': posts}))
    else:
        return HttpResponse({'error':'invalid user Please Login'})
    return HttpResponse({'oy':'oy'})

def likeit(request):
    if request.user.is_authenticated():
        print request.POST.get('fotoid')
        foto=Fotos.objects.get(id=request.POST.get('fotoid'))
        foto.likes+=1
        print foto.likes
        foto.save()
        print foto
        return HttpResponse(foto.likes)
    return HttpResponse('Sorry')


def myPosts(request):
    if request.user.is_authenticated():
        fotos = Fotos.objects.filter(author=request.user)
        print fotos
        return HttpResponse(render(request, 'posts.html', {'posts': fotos}))
    else:
        return HttpResponse({'error':'invalid user Please Login'})
    return HttpResponse({'oy':'oy'})
