#!/usr/bin/env python

from argparse import ArgumentParser
from os import listdir, getcwd, rename
from os.path import isfile, join

import re

parser = ArgumentParser(description='Rename files in current folder using regular expressions')
parser.add_argument('selector', metavar='S', help='The regular expression used to SELECT files')
parser.add_argument('replacement', metavar='R', help='The regular expression used to CHANGE the name of each file')
parser.add_argument('--sim', dest='sim', action='store_true', help='Simulate execution')

args = parser.parse_args()

sel = args.selector
rep = args.replacement
isSim = args.sim

if isSim:
    print "========= Simulation ========="

print "Selector: " + sel
print "Replacement: " + rep

execPath = getcwd()
files = [f for f in listdir(execPath) if isfile(join(execPath, f))]

print "Files in folder: " + str(len(files))

mod = 0
for file in files:
    newName = re.sub(sel, rep, file)
    if newName != file:
        if not isSim:
            rename(file, newName)
            mod += 1
        print file + " ==> " + newName

print "Files modified: " + str(mod)