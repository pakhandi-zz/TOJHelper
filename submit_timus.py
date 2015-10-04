#! /usr/bin/env python

import urllib
import urllib2
import sys

#Make sure the name of the file is same as the problem number, e.g : 1234.cpp

content = open(sys.argv[1], 'r').read()

data = {
        "Action" : "submit",
        "SpaceID" : "1",
         "JudgeID" : " ",	#Enter your judgeID
         "Language" : "28",	#Enter your language number
         "ProblemNum" : sys.argv[2],
         "Source" : content
       }

encoded_data = urllib.urlencode(data)
content = urllib2.urlopen("http://acm.timus.ru/submit.aspx?space=1",
        encoded_data)
print content.readlines()