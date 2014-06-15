#!C:\Python27\python.exe

from distutils.dir_util import copy_tree, remove_tree

import os
import sys
import getopt
import fileinput

import kegger

frameworks = ['flask', 'cherrypy', 'bottle']
framework = ''

'''
Basically, this handles the option when kegger is called.
'''
def print_error(error=None):
    print str(error)
    print 'try kegger.py <project name> to create project with default framework'
    sys.exit(2)

def tap_bunghole():
    global framework
    framework = 'flask' #default framework

    if len(sys.argv) == 1:
        print_error('No project name supplied.')

    if sys.argv[1].startswith('-'):
        try:
            opts, args = getopt.getopt(sys.argv[1:], 'hf:v', ['help', 'framework=', 'version'])
            brix_check(opts)
            project_name = sys.argv[1]
        except getopt.GetoptError as err:
            print print_error(err)
    else:
        project_name = sys.argv[1]
        if len(sys.argv) > 2:
            try:
                opts, args = getopt.getopt(sys.argv[2:], 'hf:v', ['help', 'framework=', 'version'])
            except getopt.GetoptError as err:
                print print_error(err)
            brix_check(opts)
    chug_it(project_name, framework)

def brix_check(options):
    for opt, arg in options:
        if opt in ('-h', '--help'):
            print '-h                 : for help file'
            print '-f <framework>     : to create project with basic framework'
            print '-v                 : kegger version'
            sys.exit()
        elif opt in ('-f', '--framework'):
            global framework
            framework = arg
            if framework not in frameworks:
                print 'framework name does not exist.'
                print 'valid frameworks are', frameworks
                sys.exit()
        elif opt in ('-v', '--version'):
            print 'Kegger 0.5.0'
            sys.exit()

def chug_it(project_name, framework_name):
    #first create the folder
    print 'Kegging Project ' + project_name
    path = os.path.dirname(os.path.realpath(__file__))
    components = path.split(os.path.sep)
    for i, s in enumerate(components):
        if 'kegger-' in s.lower():
            keg_index = s
    path = str.join(os.path.sep, components[:components.index(keg_index)+1])
    path_from = path + os.path.sep + "kegger" + os.path.sep + "myapp"
    path_to = os.getcwd() + os.path.sep + 'Project_' + project_name
    copy_tree(path_from, path_to)

    #frameworks
    #remove unused frameworks
    print 'scaffolding, please wait'
    #f = framework
    #sys.exit()
    for i, s in enumerate(frameworks):
        if framework not in s:
            remove_tree(path_to + os.path.sep + s + 'myappname')
    os.rename(path_to + os.path.sep + framework + 'myappname', path_to + os.path.sep + 'myappname')

    #update yaml and main
    #first part update application name. it has to be lowercase only in GAE
    print 'scaffolding, please wait.'
    fileToSearch = path_to + os.path.sep + 'app.yaml'
    for line in fileinput.input(fileToSearch, inplace=True):
        print(line.replace('application: myappname', 'application: ' + project_name.lower())),
    #second part update whatever else
    print 'scaffolding, please wait..'
    fileToSearch = path_to + os.path.sep + 'app.yaml'
    for line in fileinput.input(fileToSearch, inplace=True):
        print(line.replace('myappname', project_name)),
    fileToSearch = path_to + os.path.sep + 'main.py'
    for line in fileinput.input(fileToSearch, inplace=True):
        print(line.replace('myappname', project_name)),

    #next rename the app
    print 'scaffolding, please wait...'
    path_from = path_to + os.path.sep + 'myappname'
    path_to = path_to + os.path.sep + project_name
    os.rename(path_from, path_to)

    #update apps and models
    print 'scaffolding, please wait....'
    fileToSearch = path_to + os.path.sep + 'apps.py'
    for line in fileinput.input(fileToSearch, inplace=True):
        print(line.replace('myappname', project_name)),
    fileToSearch = path_to + os.path.sep + 'models.py'
    user_model = project_name + '_User'
    for line in fileinput.input(fileToSearch, inplace=True):
        print(line.replace('MyAppName_User', user_model)),
    fileToSearch = path_to + os.path.sep + 'views.py'
    for line in fileinput.input(fileToSearch, inplace=True):
        print(line.replace('myappname', project_name)),
    print 'Kegging completed. Enjoy.'

#main program here
if __name__ == '__main__':
    #print 'Argument List:', str(sys.argv[0:])
    tap_bunghole()
