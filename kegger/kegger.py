#!C:\Python27\python.exe

from distutils.dir_util import copy_tree

import os
import sys
import getopt
import fileinput

import kegger

'''
Basically, this handles the option when kegger is called.
'''
def tap_bunghole():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ho:v', ['help', 'output='])
    except getopt.GetoptError as err:
        print str(err)
        print 'example python kegger.py -o <project name>'
        sys.exit(2)
    if opts:
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print '-o <project name>  : to create project'
                print '-h                 : for help file'
                print '-v                 : kegger version'
                sys.exit()
            elif opt == '-v':
                print 'Kegger 0.3'
                sys.exit()
            elif opt in ('-o', '--output'):
                chug_it(arg)
    else:
        #kegger with no options means create new project
        chug_it(sys.argv[1])

def chug_it(project_name):
    #first create the folder
    print 'creating Project ' + project_name
    path = os.path.dirname(os.path.realpath(__file__))
    components = path.split(os.sep)
    path = str.join(os.sep, components[:components.index("kegger-0.4.1-py2.7.egg")+1])
    path_from = path + os.sep + "kegger" + os.sep + "myapp"
    print 'scaffolding, please wait'
    path_to = os.getcwd() + '\\Project_' + project_name
    copy_tree(path_from, path_to)

    #update yaml and main
    #first part update application name. it has to be lowercase only in GAE
    fileToSearch = path_to + '\\app.yaml'
    for line in fileinput.input(fileToSearch, inplace=True):
        print(line.replace('application: myappname', 'application: ' + project_name.lower())),
    #second part update whatever else
    fileToSearch = path_to + '\\app.yaml'
    for line in fileinput.input(fileToSearch, inplace=True):
        print(line.replace('myappname', project_name)),
    fileToSearch = path_to + '\\main.py'
    for line in fileinput.input(fileToSearch, inplace=True):
        print(line.replace('myappname', project_name)),

    #next rename the app
    path_from = path_to + '\\myappname'
    path_to = path_to + '\\' + project_name
    os.rename(path_from, path_to)

    #update apps and models
    fileToSearch = path_to + '\\apps.py'
    for line in fileinput.input(fileToSearch, inplace=True):
        print(line.replace('myappname', project_name)),
    fileToSearch = path_to + '\\models.py'
    user_model = project_name + '_User'
    for line in fileinput.input(fileToSearch, inplace=True):
        print(line.replace('MyAppName_User', user_model)),

#main program here
if __name__ == '__main__':
    #print 'Argument List:', str(sys.argv[0:])
    tap_bunghole()