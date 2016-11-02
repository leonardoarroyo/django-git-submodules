import sys
import os
import __main__
import glob

prop = '__file__'

def get_project_root():
  path = getattr(__main__, prop)
  return os.path.dirname(os.path.abspath(path))

def add(submodules):
  if not isinstance(submodules, (list, tuple, )):
    submodules = [submodules]

  PROJECT_ROOT = get_project_root()

  for mod in submodules:
    path = os.path.abspath(os.path.join(PROJECT_ROOT, mod))
    sys.path.insert(0, path)

def locate(string):
  return glob.glob(os.path.join(get_project_root(), string))
