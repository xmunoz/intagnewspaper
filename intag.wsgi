import sys, os, inspect
projectpath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(projectpath)
from routes import app as application
