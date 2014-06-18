from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

#jinja2 templating stuff
from jinja2 import Environment, FileSystemLoader

def url_for(endpoint, **values):
    filename = values.pop('filename')
    return endpoint + "/" + filename

env = Environment(loader=FileSystemLoader('myappname/templates'))
env.globals['url_for'] = url_for

#import our models
from models import *


config = Configurator()

def hello(request):
    template = env.get_template('index.html')
    return Response(template.render())
config.add_route('home', '/')
config.add_view(hello, route_name='home')


def Sign_Up(request):
    error = ''
    if request.method == 'POST':
        if Register(request.POST.get('full_name'),
                    request.POST.get('email'),
                    request.POST.get('password'),
                    request.POST.get('phone_no')):
            return Log_User_In(request.POST.get('email'))
        else:
            error = 'Email already in use'
    # was GET or the credentials were invalid
    template = env.get_template('sign-up.html')
    return Response(template.render(error=error))
config.add_route('signup', '/Sign-Up')
config.add_view(Sign_Up, route_name='signup')

def Register(new_full_name, new_email, new_password, new_phone_no):
    user = Users.get_by_id(new_email)

    if not user:
        new_user = Users(id=new_email)

        new_user.password = new_password
        new_user.full_name = new_full_name
        new_user.phone_no = new_phone_no
        new_user.put()
        return True
    else:
        return False


def Sign_Out(request):
    template = env.get_template('sign-in.html')
    return Response(template.render())
config.add_route('signout', '/Sign-Out')
config.add_view(Sign_Out, route_name='signout')


def Sign_In(request):
    error = ''
    if request.method == 'POST':
        if Authenticate(request.POST.get('email'),
                       request.POST.get('password')):
            return Log_User_In(request.POST.get('email'))
        else:
            error = 'Invalid email or password'
    # was GET or the credentials were invalid
    template = env.get_template('sign-in.html')
    return Response(template.render(error=error))
config.add_route('sign_in', '/Sign-In')
config.add_view(Sign_In, route_name='sign_in')

def Authenticate(check_email, check_password):
    user = Users.get_by_id(check_email)

    if user:
        if user.password == check_password:
           return True
    return False


def Log_User_In(email): # goes to dashboard page
    #do user login stuff here like setting sessions, etc
    return HTTPFound(location='/Dashboard')


def Dashboard(request):
    template = env.get_template('dashboard.html')
    return Response(template.render())
config.add_route('dashboard', '/Dashboard')
config.add_view(Dashboard, route_name='dashboard')