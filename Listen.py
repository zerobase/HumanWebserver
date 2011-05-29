import HumanWebserver

try:
	humanServer = HumanWebserver.HumanWebserver()
	humanServer.start(8008)
except KeyboardInterrupt:
	del humanServer
