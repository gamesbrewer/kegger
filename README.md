#KEGGER
======

Use your Favourite Python Frameworks on Google AppEngine <br />
Flask, Bottle <br />
CherryPy *To be Done <br />

##Pre-Requisites
=============
1. Python 2.7 <br />
Get it here https://www.python.org/download/releases/2.7 <br />

2. Google App Engine SDK <br />
Get it here https://developers.google.com/appengine/downloads <br />

##How To Use
=============
###WINDOWS
Installation <br />
step 1 enter: <br />
C:\> unzip kegger-master.zip<br />

step 2 enter: <br />
C:\>cd kegger-master <br />

step 3 enter: <br />
C:\>kegger-master\python setup.py install <br />

That's it! If it installed, congratulations! <br />

Checking Version <br />
C:\>kegger.py -v <br />

Creating Project <br />
C:\>kegger.py WhalePopulationCount -f bottle<br />
(This will create C:\>Project_WhalePopulationCount folder with everything you need in it) <br />

-------------

###UBUNTU
(if you get -bash: unzip: command not found then sudo apt-get install unzip) <br />

Installation <br />
step 1 enter: <br />
/home# unzip kegger-master.zip -d destination_folder <br />

step 2 enter: <br />
/home# cd kegger-master <br />

step 3 enter: <br />
/home# python setup.py install <br />

That's it! If it installed, congratulations! <br />

Checking Version <br />
/home# kegger.py -v <br />

Creating Project <br />
/home# kegger.py WhalePopulationCount -f bottle <br />
(This will create /home/Project_WhalePopulationCount# directory with everything you need in it) 


##TODO, WISHLIST, AND STUFF
=============
1. Add switcher for webframeworks. eg. kegger.py  -o WhalePopulationCount -f Grok (to create Project WhalePopulationCount using Grok framework) <br />
2. Frameworks to be added Grok, Pyramid, Glasshammer, Pylatte, Watson, Bottle, CherryPy. Obviously some runs on only 3.x so....
3. Currently 2.7 compliant. Need to make it 3.x compliant.




