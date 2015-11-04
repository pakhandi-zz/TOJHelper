#TIMUS ONLINE JUDGE
import requests
import os
from bs4 import BeautifulSoup
import shutil

#print "Enter question no."
qno=raw_input();

url="http://acm.timus.ru/problem.aspx?space=1&num="+qno
print url

flag=0
try:
    data=requests.get(url)
    flag=1
except Exception,e:
    print "Direct Connection Failed,trying Proxy"
    f=open("proxy.txt","r+")
    http_proxy=f.read(100)
    f.close()

    proxyDict={
		"http":"http://"+http_proxy
	      }
    data=requests.get(url,proxies=proxyDict)
    flag=1

if flag==0:
    print "Error in Connection"
    print "hena"


soup=BeautifulSoup(data.text)




for tbl in soup.findAll('table','sample'):
    if (os.path.exists(qno)):
        print "Folder Exists"
    else:
        os.makedirs(qno)  

    detach_dir=qno+"/"
    incounter=1
   
    for item in tbl.findAll('pre','intable'):
        if incounter%2 == 1:
            att_path=os.path.join(detach_dir,"in"+str((incounter/2))+".txt")
            print att_path
            fo=open(att_path,'wb')
        else:
            att_path=os.path.join(detach_dir,"out"+str((incounter/2)-1)+".txt")
            print att_path
            fo=open(att_path,'wb')
        incounter+=1
        item=str(item).replace("<pre class=\"intable\">","")
        item=str(item).replace("</pre>","")
        item=str(item).replace("<br/>","\n")
        fo.write(item)
