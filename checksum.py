#!/usr/bin/env python3

import argparse
import hashlib

parser = argparse.ArgumentParser(description="Validate checksum of files")

parser.add_argument('-encryption', dest="enc", default="sha1")
parser.add_argument('-checksum', dest="cs", default="")
parser.add_argument('-file', dest="fPath", default="")

args=parser.parse_args()

encString = args.enc.lower()

if (encString == "sha256"):
    hasher = hashlib.sha256()
elif (encString == "md5"):
    hasher = hashlib.md5()
else:
    hasher = hashlib.sha1()

def h(fName):
    with open(fName, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def matches(one,two):
    return one == two

#print (encryption)
result = h(args.fPath)
print ('')
print ('')
print ('file: %s' % args.fPath)
print ('%s hash: %s' % (args.enc,result))
print ('expected: %s' % args.cs)
print ('')
print ('match: %s' % matches(result,args.cs))
#assert result is args.cs
