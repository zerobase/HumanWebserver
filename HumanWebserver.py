import socket, sys, subprocess, os, select, socket, readline, time

class HumanWebserver:
	responseFile = os.getcwd() + "/response.txt"
	responseHttp = "HTTP/1.1 %d %s\r\nContent-Type: text/html\r\n\r\n\r\n"

	statusCodes = {
		100: "Continue",
		101: "Switching Protocols",
		102: "Processing",
		200: "OK",
		201: "Created",
		202: "Accepted",
		203: "Non-Authoritative Information",
		204: "No Content",
		205: "Reset Content",
		206: "Partial Content",
		207: "Multi-Status",
		300: "Multiple Choice",
		301: "Moved Permanently",
		302: "Found",
		303: "See Other",
		304: "Not Modified",
		305: "Use Proxy",
		307: "Temporary Redirect",
		400: "Bad Request",
		401: "Unauthorized",
		402: "Payment Required",
		403: "Forbidden",
		404: "Not Found",
		405: "Method Not Allowed",
		406: "Not Acceptable",
		407: "Proxy Authentication Required",
		408: "Request Time-out",
		409: "Conflict",
		410: "Gone",
		411: "Length Required",
		412: "Precondition Failed",
		413: "Request Entity Too Large",
		414: "Request-URI Too Long",
		415: "Unsupported Media Type",
		416: "Requested range not satisfiable",
		417: "Expectation Failed",
		418: "I'am a Teapot",
		421: "There are too many connections from your internet adress",
		422: "Unprocessable Entity",
		423: "Locked",
		424: "Failed Dependency",
		425: "Unordered Collection",
		426: "Upgrade Required",
		500: "Internal Server Error",
		501: "Not Implemented",
		502: "Bad Gateway",
		503: "Service Unavailable",
		504: "Gateway Time-out",
		505: "HTTP Version not supported",
		506: "Variant Also Negotiates",
		507: "Insufficient Storage",
		508: "Bandwith Limit Exceeded",
		510: "Not Extended"
	}
<<<<<<< HEAD
	
	def __init__(self):		
=======

	def __init__(self, port):
		try:
			port = int(port)
		except:
			print (port, " ist kein gueltige Portnummer")
			sys.exit(1)

		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind(('', port))

>>>>>>> 21332bcc1994007def05320d907010441fe25790
		completer = self.Completer(self.statusCodes)
		readline.parse_and_bind("tab: complete")
		readline.set_completer(completer.complete)

	def __del__(self):
		self.stop()

	def stop(self):
<<<<<<< HEAD
		if self.socket != None:
			self.socket.close()		
	
	def start(self, port):
		try:
			port = int(port)
		except:
			print (port, " ist kein gueltige Portnummer")
			sys.exit(1)
		
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind(('', port))
		
=======
		self.socket.close()

	def start(self):
>>>>>>> 21332bcc1994007def05320d907010441fe25790
		print ("World's Fastest Web Server HumanWebserver started")
		self.socket.listen(1)

		try:
			while 1:
				conn, addr = self.socket.accept()
<<<<<<< HEAD
				cfile = conn.makefile("rw", 0)
				
				#print ("Verbindung von Host: ", addr[0], " port ", addr[1])
				
				data = self.recvall(conn)
				print (bytes.decode(data))
								
=======
				print ("Verbindung von Host: ", addr[0], " port ", addr[1])
				data = conn.recv(4096)
				if not data: break

				print (bytes.decode(data))

>>>>>>> 21332bcc1994007def05320d907010441fe25790
				while True:
					status = raw_input("Respond with? ")
					if status == "":
						status = 200
						break;
					try:
						status = int(status)

						if self.statusCodes.has_key(status):
							break;
					except:
						pass
<<<<<<< HEAD
						
					print "%s ist kein gueltiger Status"%status					
				
				cfile.write(self.content(self.responseFile, self.responseHttp%(status, self.statusCodes[status])))	
				cfile.close()
				conn.close()
				
=======
					finally:
						print "%s ist kein gueltiger Status"%status

				f = open(self.responseFile, 'w')
				f.write(self.responseHttp%(status, self.statusCodes[status]))
				f.close()

				p = subprocess.Popen("vim %s +" % self.responseFile, bufsize=2048, shell=True)
				p.wait()

				f = open(self.responseFile, 'r')
				conn.send(f.read())	
				conn.close()
				f.close()

>>>>>>> 21332bcc1994007def05320d907010441fe25790
				os.remove(self.responseFile)

		except KeyboardInterrupt:
			print("\nShutting down ...")
		finally:
			self.stop()
<<<<<<< HEAD
	
	def content(self, path, default = ""):
		f = open(path, 'w')
		f.write(default)
		f.close()

		p = subprocess.Popen("vim %s +" % path, bufsize=2048, shell=True)
		p.wait()

		f = open(path, 'r')
		
		content = f.read()
		f.close()
		
		return content
	
	def recvall(self, the_socket, timeout=''):
		#setup to use non-blocking sockets
		#if no data arrives it assumes transaction is done
		#recv() returns a string
		the_socket.setblocking(0)
		total_data=[];data=''
		begin=time.time()
		
		if not timeout:
			timeout=1
			
		while 1:
			#if you got some data, then break after wait sec
			if total_data and time.time()-begin>timeout:
				break
			#if you got no data at all, wait a little longer
			elif time.time()-begin>timeout*2:
				break
			wait=0
			try:
				data=the_socket.recv(4096)
				if data:
					total_data.append(data)
					begin=time.time()
					data='';wait=0
				else:
					time.sleep(0.1)
			except:
				pass
			#When a recv returns 0 bytes, other side has closed
		
		result=''.join(total_data)
		return result
	
=======


>>>>>>> 21332bcc1994007def05320d907010441fe25790
	class Completer:
		def __init__(self, dictionary):
			self.dictionary = dictionary
			self.prefix = None

		def complete(self, prefix, index):
			if prefix != self.prefix:
				self.matching_words = [(k, v) for (k, v) in self.dictionary.items() if str(k).startswith(prefix)]
				self.prefix = prefix

			try:
				if (len(self.matching_words) > 1):
					return "%s %s"%(str(self.matching_words[index][0]), self.matching_words[index][1])
				else:
					return str(self.matching_words[index][0])
			except IndexError:
				return None

<<<<<<< HEAD




















=======
try:
	humanServer = HumanWebserver(2000)
	humanServer.start()
except KeyboardInterrupt:
	del humanServer
>>>>>>> 21332bcc1994007def05320d907010441fe25790
