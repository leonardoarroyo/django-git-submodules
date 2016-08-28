import sys
import os
import __main__

def add(submodule):
  PROJECT_ROOT = os.path.dirname(os.path.abspath(__main__.__file__))
  path = os.path.abspath("{}/{}/".format(PROJECT_ROOT, submodule))
  sys.path.append(path)
