import socket			
print('This only tests if port 22 is open\n')
s = socket.socket()		 
try:
  port = 22	
  s.connect(('127.0.0.1', port))
except:
    print('port closed')
print (s.recv(1024).decode())
# close the connection 
s.close()	 
	

