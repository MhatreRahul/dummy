#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def sort_urls(url):
  return url.key


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  match=re.search(r'_(.+)',filename)
  hostname=match.group(1)

  urls={}
  fh=open(filename,'r')
  match=re.findall(r'GET (\S+-(\S+?).jpg)',fh.read())
  fh.close()
  for url in match:
    urls[url[1]]="http://"+hostname+url[0]

  list=[]
  surls=sorted(urls)
  for url in surls:
    list.append(urls[url])

  return list
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  #Create directory if it does not exist
  if not os.path.exists(dest_dir):
    print "directory "+dest_dir+" does not exist. Creating new directory"
    os.mkdir(dest_dir)
  if len(os.listdir(dest_dir)) != 0:
    print("Directory is not empty. Provide an empty dir or create new dir")
    print "Exiting program"
    sys.exit()

  index = file(os.path.join(dest_dir, 'index.html'), 'w')
  index.write('<html><body>\n')

  i=0
  for img_url in img_urls:
    filename='img%d'%i
    print "Downloading "+img_url+ "at "+filename
    urllib.urlretrieve(img_url,os.path.join(dest_dir,filename) )
    i+=1
    index.write('<img src="%s">' % filename)

  index.write('\n</body></html>\n')
  index.close()

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
