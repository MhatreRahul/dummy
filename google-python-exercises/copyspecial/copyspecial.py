#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def copy_s2d(source,dest):
  try:
    src=os.path.abspath(source)
  except:
    sys.stderr.write('Problem finding source directory:' + source)
  if not os.path.exists(dest):
    sys.stderr.write('Destination directory does not exist, creating dir:'+dest)
    os.mkdir(dest)
  abs_dest=os.path.abspath(dest)

  cmd = 'cp -r '+src+' ' +abs_dest
  print 'Copying', src, 'to', abs_dest, 'Cmd :',cmd,'\n'

  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write('Problem in copying dir')
  else:
    sys.stderr.write('Source copied to' + abs_dest)

def zip_dir(source,zipfile):
  try:
    src=os.path.abspath(source)
  except:
    sys.stderr.write('Problem finding source directory:' + source)
  cmd = 'tar -cvzf ' + zipfile +' '+ source
  print "Zip command to run:", cmd
  (status, output) = commands.getstatusoutput(cmd)

  if status:
    sys.stderr.write('Problem in zipping dir')
  else:
    sys.stderr.write('Zip file created at'+os.path.abspath(zipfile))


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if todir:
    copy_s2d(args[0],todir)
  if tozip:
    zip_dir(args[0],tozip)
  
if __name__ == "__main__":
  main()
