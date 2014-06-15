from bottle import Bottle, route, request

#jinja2 templating stuff
from jinja2 import Environment, FileSystemLoader

def url_for(endpoint, **values):
    filename = values.pop('filename')
    return endpoint + "/" + filename

env = Environment(loader=FileSystemLoader('myappname/templates'))
env.globals['url_for'] = url_for

#import our models
from models import *

app = Bottle()

@app.route('/')
def hello():
    template = env.get_template('index.html')
    return template.render()


@app.get('/Sign-Up')
def Sign_Up():
    template = env.get_template('sign-up.html')
    return template.render()

@app.post('/Sign-Up')
def Do_Sign_Up():
    error = ''
    if Register(request.forms.get('full_name'),
                request.forms.get('email'),
                request.forms.get('password'),
                request.forms.get('phone_no')):
        return Log_User_In(request.forms.get('email'))
    else:
        error = 'Email already in use'
    template = env.get_template('sign-up.html')
    return template.render(error=error)

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


@app.route('/Sign-Out')
def Sign_Out():
    template = env.get_template('sign-in.html')
    return template.render()


@app.get('/Sign-In')
def Sign_In():
    template = env.get_template('sign-in.html')
    return template.render()

@app.post('/Sign-In')
def Do_Sign_In():
    error = ''
    if Authenticate(request.forms.get('email'),
                    request.forms.get('password')):
        return Log_User_In(request.forms.get('email'))
    else:
        error = 'Invalid email or password'
    return render_template('sign-in.html', error=error)

def Authenticate(check_email, check_password):
    user = Users.get_by_id(check_email)

    if user:
        if user.password == check_password:
           return True
    return False

def Log_User_In(email): # goes to dashboard page
    template = env.get_template('dashboard.html')
    return template.render()


@app.route('/Dashboard')
def Dashboard():
    return render_template('dashboard.html')