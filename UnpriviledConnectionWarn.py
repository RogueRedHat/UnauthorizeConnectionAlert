import socket			 
import subprocess

s = socket.socket()		 
print ("Socket successfully created\n")
try:
    port = 22
    s.bind(('', port))
except :
    port = 25
    s.bind(('',port))


print ("socket desiguse as  %s" %(port)) 

s.listen(5)	 
print ("\nWaiting\n")		  
while True: 
  c, addr = s.accept()
  subprocess.call(["notify-send", f"WARNING SOMEONE IS CONNECT TO PORT: {port}"])
  print (addr, "is trying to connect to port",port )
  c.close()


