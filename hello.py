#!/usr/bin/python


import os
import cgi, cgitb

cgitb.enable()

form = cgi.FieldStorage()

message="meow"

#get the fileitem
fileitem=form['userfile']
if fileitem.file:
    #yay...we got a file
    message=fileitem.file.read()




f=open('new.std','w')
f.write(message)
f.close()

os.system('./Main new.std>file 2>file2')

print """\
Content-Type: text/html\n
<html><body>"""

f=open('file2','r')
m=f.read()

if(m):
	pass
else:
	m="succesfull"
	
print("""
<h1>Message</h1>
<a href=index.html > Main page</a> 
<p>%s</p>
</body></html>
""" % (m))

f.close()
os.system('rm file*')
os.system('rm new.std')
