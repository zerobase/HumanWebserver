import socket, sys, os
import HumanWebserver

if len(sys.argv) != 3:
	print "Usage: python %s <host> <port>"%sys.argv[0]
	sys.exit(1)

try:
	port = int(sys.argv[2])
except:
	print "%s ist kein gueltige Portnummer"%sys.argv[2]
	sys.exit(1)


humanServer = HumanWebserver.HumanWebserver()
requestHttp = "GET / HTTP/1.0\r\nUser-Agent: HumanWebserver\r\nHost: %s:%d\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n\r\n"%(sys.argv[1], port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], port))
s.send(humanServer.content(os.getcwd() + "/request.txt", requestHttp))
data = humanServer.recvall(s)
print data
s.close()
