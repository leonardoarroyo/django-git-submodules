import sys
import os
import __main__
import glob

def get_project_root():
  return os.path.dirname(os.path.abspath(__main__.__file__))

def add(submodules):
  if not isinstance(submodules, (list, tuple, )):
    submodules = [submodules]

  PROJECT_ROOT = get_project_root()

  for mod in submodules:
    path = os.path.abspath(os.path.join(PROJECT_ROOT, mod))
    print(path)
    sys.path.insert(0, path)

def locate(string):
  return glob.glob(os.path.join(get_project_root(), string))
