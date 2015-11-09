#TIMUS ONLINE JUDGE
import mechanize
import re
import os
from bs4 import BeautifulSoup
#print "Enter question no."
qno=raw_input();
myurl="http://acm.timus.ru/problem.aspx?num="+qno

br=mechanize.Browser()

br.set_proxies({"http":"edcguest:edcguest@172.31.102.14:3128"})

br.set_handle_robots(False)

response=br.open(myurl)
print response.code

br.addheaders=[('User-agent','Firefox')]

response=br.open(myurl)


soup=BeautifulSoup(response)


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

