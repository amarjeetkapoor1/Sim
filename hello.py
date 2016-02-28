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

print "Content-Type:application/octet-stream; name=\"file\"\r\n";
print "Content-Disposition: attachment; filename=\"file\"\r\n\n";

	

print("""
<h1>Message</h1>
<a href=index.html > Main page</a><br>
<a href=file>see csv output file</a>  
<p>%s</p>
</body></html>
""" % (m))

f.close()
os.system('rm new.std')
