import sys
sys.path.append('~lib/')
from decimal import *
from lib import *
import bitcoinrpc
import socket
import json
import urllib2
import subprocess
import time

settings_dict = configure_settings()

pool_file = open("pool.conf", "r")
cg_pool = "cd CGMiner\ncgminer.exe "
count  = 0

pool_response = pool_file.read()

pool_file.close()

pool_response = json.loads(pool_response)

coin_collection = {}

print '---'
print 'Starting JSON Read from pool conf and coin objects'
print '---'
#reading json from pool.conf and adding information to coin objects
if settings_dict['cg_start'] == '1':
	for key in pool_response.iterkeys():
		if pool_response[key]['type'] == settings_dict['mining_kernel']:
			cg_pool += '-o ' + pool_response[key]['url'] + ' -u ' + pool_response[key]['user'] + ' -p ' + pool_response[key]['pass'] + ' '
			coin_collection[key] = Coin(pool_response[key]['name'], count, pool_response[key]['url'], pool_response[key]['user'], pool_response[key]['pass'], pool_response[key]['halving'], pool_response[key]['blockCalc'], pool_response[key]['type'], '', 0.0, key, '', pool_response[key]['port'], pool_response[key]['initialReward'], int(pool_response[key]['minimum']))
			count += 1
	bat_out = open('cgminer.bat', 'w')
	bat_out.write(cg_pool + settings_dict['cg_set'])
	bat_out.close()

coin = 'No Pool'
pool = -1
daily = -1

while True:
	print 'Finished reading pool conf to coin objects'
	print '---'
	print 'Starting Cryptsy Info Parse'
	print '---'

	#gathering cryptsy exchange info
	marketData = urllib2.urlopen(urllib2.Request('http://pubapi.cryptsy.com/api.php?method=marketdatav2'))

	response = json.loads(marketData.read())

	exchange_info = {}
	coinInfo = {}

	for key in response.iterkeys():
		returnDict = response[key]
		if isinstance(returnDict, dict):
			for returnKey in returnDict.iterkeys():
				marketbook = returnDict[returnKey]
		        if isinstance(marketbook, dict):
		            for marketKey, marketData in marketbook.iteritems():
		            	if marketData['secondarycode'] == 'BTC':
			                coinInfo = {"marketid":marketData["marketid"], "price":marketData["lasttradeprice"], "secondarycode":marketData["secondarycode"]}
			                exchange_info[marketData['primarycode']] = coinInfo

	for key in exchange_info.iterkeys():
		print key
		print exchange_info[key]['price']


	#filling in missing exchange info
	for key in coin_collection.iterkeys():
		if key in exchange_info.keys():
			coin_collection[key].setMarketid(exchange_info[key]['marketid'])
			coin_collection[key].setPrice(exchange_info[key]['price'])
			coin_collection[key].setSecondary(exchange_info[key]['secondarycode'])

	print 'Finished Cryptsy Info Parse'
	print '---'
	print 'Opening new cgminer mining window'
	print '---'

	p = subprocess.Popen('cgminer.bat', creationflags=subprocess.CREATE_NEW_CONSOLE)

	print 'cgminer window opened'
	print '---'
	print 'Looping through coins to determine most profitable'
	print '---'

	print 'Entering pool determination while loop'
	print '---'
	for key in coin_collection.iterkeys():
		print 'Crunching numbers for: ', coin_collection[key].getName()
		print '---'
		coin_collection[key].crunchNumbers()
		if coin_collection[key].getDailyBTC() > daily:
			print 'switching from', coin, ' to ', coin_collection[key].getName()
			print '---'
			coin = coin_collection[key].getName()
			daily = coin_collection[key].getDailyBTC()
			pool = coin_collection[key].getPoolNumber()
	time.sleep(7)
	print 'Switching to pool: ', pool
	print '---'

	switchpool(pool)

	time.sleep(420)

	print 'Exited pool determination while loop'
