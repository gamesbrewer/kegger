import os
import sys

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'libs'))

from myappname import apps

app = apps.create_app()