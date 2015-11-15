#TIMUS ONLINE JUDGE
import mechanize
import re
import os
import shutil
from bs4 import BeautifulSoup
#print "Enter question no."
qno=raw_input();
#qno=sys.argv[1]
myurl="http://acm.timus.ru/problem.aspx?num="+qno

br=mechanize.Browser()

#Format:br.set_proxies({"http":"username:password@proxy:port"})
br.set_proxies({"http":"edcguest:edcguest@172.31.100.26:3128"})

br.set_handle_robots(False)

response=br.open(myurl)
print response.code

br.addheaders=[('User-agent','Firefox')]

response=br.open(myurl)
#print response.read()

soup=BeautifulSoup(response)
print br.title()

for tbl in soup.findAll('table','sample'):
    if (os.path.exists(qno)):
        print "Folder Exists"
    else:
        os.makedirs(qno)  

    shutil.copyfile("zz.sh",qno+"/zz.sh")
    shutil.copyfile("zy.sh",qno+"/zy.sh")
    shutil.copyfile("zx.sh",qno+"/zx.sh")
    shutil.copyfile("temp.txt",qno+"/qno.txt")
    shutil.copyfile("template.cpp", qno+"/prog.cpp" )    

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

