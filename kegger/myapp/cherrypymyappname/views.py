import cherrypy
import jinja2

from models import *

def render_template(filename, **template_args):
    response.write(jinja2.render_template(filename, **template_args))

def hello(self):
    return render_template('index.html')
index.exposed = True

'''
@general.route('/')
def hello():
    return render_template('index.html')


@general.route('/Sign-Up', methods=['POST', 'GET'])
def Sign_Up():
    error = ''
    if request.method == 'POST':
        if Register(request.form['full_name'],
                    request.form['email'],
                    request.form['password'],
                    request.form['phone_no']):
            return Log_User_In(request.form['email'])
        else:
            error = 'Email already in use'
    # was GET or the credentials were invalid
    return render_template('sign-up.html', error=error)


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


@general.route('/Sign-Out')
def Sign_Out():
    return render_template('sign-in.html')


@general.route('/Sign-In', methods=['POST', 'GET'])
def Sign_In():
    error = ''
    if request.method == 'POST':
        if Authenticate(request.form['email'],
                       request.form['password']):
            return Log_User_In(request.form['email'])
        else:
            error = 'Invalid email or password'
    # was GET or the credentials were invalid
    return render_template('sign-in.html', error=error)


def Authenticate(check_email, check_password):
    user = Users.get_by_id(check_email)

    if user:
        if user.password == check_password:
           return True
    return False


def Log_User_In(email): # goes to dashboard page
    return render_template('dashboard.html')


@general.route('/Dashboard')
def Dashboard():
    return render_template('dashboard.html')
'''