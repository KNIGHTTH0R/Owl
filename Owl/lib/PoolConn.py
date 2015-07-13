import sys
import socket
import json

#add a pool to cgminer by passing in addpool(poolurl + ',' + pooluser + ',' + userpassword)
def addpool(arg=None):
	commandCG('addpool', arg)

#switch a pool in cgminer, pass in pool number corresponding to currency code from pool_dict eg. 'LTC' could be pool 1
#switchpool(pool_dict['LTC']) to switch to predefined Litecoin pool
def switchpool(arg=None):
	commandCG('switchpool', arg)

def poolstatus(arg='POOLS'):
	commandCG('pools', arg)

def commandCG(command, arg=None):

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('127.0.0.1', 4028))

	payload = {'command': command}
	payload.update({'parameter': unicode(arg)})

	sock.send(json.dumps(payload))

	received = ""
	chunk = ""
	while True:
		chunk = sock.recv(1024)
		if chunk == '':
			break
		received = received + chunk

	#checkpools(received)

def checkpools(received):

	print received
	str(received)
	help(received)

