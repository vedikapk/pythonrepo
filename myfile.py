import os
import urllib
import re
import string
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

""" os.system("start \"\" http://mirror.centos.org/centos/6/updates/x86_64/Packages/")
<tr>
<td valign="top"><img src="/icons/unknown.gif" alt="[   ]"></td>
<td><a href="java-1.7.0-openjdk-1.7.0.141-2.6.10.1.el6_9.x86_64.rpm">java-1.7.0-openjdk-1.7.0.141-2.6.10.1.el6_9.x86_64.rpm</a></td>
<td align="right">2017-05-09 16:59  </td>
<td align="right"> 26M</td>
<td>&nbsp;</td>
</tr>
"""
link = "http://mirror.centos.org/centos/6/updates/x86_64/Packages/"
f = urllib.urlopen(link)
myfile = f.read()
print(type(myfile))

class countRepo(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.count = 0
        
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href" and value.endswith(".rpm"):
                   self.count += 1

    def handle_data(self, data):
        
        if int(self.count) > data:
            data = int(self.count)
            return data
            
parser = countRepo()
parser.feed(myfile)
max1 = 0
sr = parser.handle_data(max1)
print "Number of packages present : ", sr

soup = BeautifulSoup(myfile)
table_tag = soup.findAll('table')[2]
st = []
for row in table_tag.findAll('tr'):
    col = row.findAll('td')
    for c in col:
        st.append(c.get_text())
print type(st)
countofmb = 0.0
countofkb = 0.0
count = 0.0
a = []
b = []
for i in range(8,2240,5):
    if(st[i].endswith("M")):
        a = st[i].split("M")
        countofmb += float(a[0])
    else:
        b = st[i].split("K")
        countofkb += float(b[0])

count = (countofmb * 1024) + countofkb
print "combined size of packages : " , count , "KB"
print "combined size of packages : " , count/1024 , "MB"




