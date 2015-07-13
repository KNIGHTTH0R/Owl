import sys
import bitcoinrpc
import datetime

def setExternal(code, blockcount, halving, blockreward):
	if code=='BUK':
		return getBUKBlock()
	elif code=='DMC':
		return getDMCBlock()
	elif code=='DRK':
		return getDRKBlock()
	elif code=='EMC2':
		return getEMC2Block()
	elif code=='TIPS':
		return getTIPSBlock()
	elif code=='JKC':
		return getJKCBlock()
	elif code=='KDC':
		return getKDCBlock()
	elif code=='MST':
		return getMSTBlock()
	elif code=='MOON':
		return getMOONBlock()
	elif code=='NET':
		return getNETBlock()
	elif code=='PTS':
		return getPTSBlock()
	elif code=='TIX':
		return getTIXBlock()
	elif code=='PHS':
		return getPHSBlock()
	elif code=='SMC':
		return getSMCBlock()
	elif code=='NOBL':
		return getNOBLBlock()
	elif code=='42':
		return get42Block(blockcount)
	else:
		print 'Either coin is not coded or coin got passed to external when it should have been passed to internal'
		with open("errorlog.txt", "w+") as errorlog:
			errorlog.write(datetime.datetime.now() + ": Either coin is not coded or coin got passed to external when it should have been passed to internal")
		errorlog.close()

def get42Block(blockcount):
	return 0.000042


def genBlockReward(blockCount, halving, blockReward):
	blockCount = (blockCount - (blockCount % halving)) / halving

	for i in range(0, int(blockCount)):
		blockReward = blockReward / 2.0

	return blockReward	

#Bitcoin
def getBTCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'testing', host='127.0.0.1', port=3881)

	blockCount = conn.getblockcount()
	
	return genBlockReward(blockCount, 210000.0, 50.0)

#Litecoin
def getLTCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'testing', host='127.0.0.1', port=3882)

	blockCount = conn.getblockcount()
		
	return genBlockReward(blockCount, 840000.0, 50.0)

#Dogecoin
def getDOGEBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='50.66.72.155', port=22555)

	blockCount = conn.getblockcount()

	if blockCount >= 600000:
		return 10000
	else:
		return genBlockReward(blockCount, 100000.0, 500000.0)	

#Batcoin
def getBATBlock():
	return 60000

#BBQCoin
def getBQCBLock():
	conn = bitcinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()
	
	return genBlockReward(blockCount, 24000000.0, 42)

#Benjamin
def getBENBlock():
	conn = bitcinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return	genBlockReward(blockCount, 64000.0, 100.0)

#betacoin
def getBETBlock():
	conn = bitcinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 126000.0, 128.0)

#bitgem
def getBTGBlock():
	pass

#bottecaps
def getCAPBlock():
	return 10

#bytecoin
def getBTEBlock():
	return 50

#cachecoin
def getCACHBlock():
	pass
	#need to figure this one out

#crypto-cash
def getCASHBlock():
	pass
	#think ill skip to complex

#casinocoin
def getCSCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=47970)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 3153600.0, 50.0)

#chinacoin?
def getCHNBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 2628000.0, 88.0)

#colossuscoin
def getCOLBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 50000.0, 5000000.0)

#continuumcoin
def  getCTMBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	blockReward = genBlockReward(blockCount, 86400.0, 524288.0)

	if blockReward < 1:
		return 1
	else:
		return blockReward

#copperbars
#double check with randy about reward
def getCPRBlock():
	return 0.0064

#cosmoscoin
def getCMCBlock():
	return 3.5

#craftcoin
def getCRCBlock():
	return 10

#cryptobuck
def getBUKBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount <= 300:
		return 1
	elif blockCount <= 35000:
		return 33
	elif blockCount <= 70000:
		return 22
	else:
		return 11

#cryptogenicbullion
def getCGBBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	blockReward = genBlockReward(blockCount, 43200.0, 10)

	if blockReward < 0.01:
		return 0.01
	else:
		return blockReward

#damacoin
def getDMCBlock():	
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount < 50000:
		return 200000
	elif blockCount < 100000:
		return 100000
	elif blockCount < 200000:
		return 50000
	elif blockCount < 400000:
		return	25000
	else:
		return 20000

#darkcoin
#chack to make sure its returning integer not decimal
def getDRKBlock():	
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	difficulty = conn.getdifficulty()

	return int(2222222 / (((difficulty + 2600) / 9) ** 2))

#diamondcoin
def getDMDBlock():
	return 1.0416

#digibyte
def getDGBBlock():
	pass
	#emailed them about it

#digitacoin
def getDGCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 4730400, 15)

#doubloons
def getDBLBlock():
	return 6.77

#earthcoins
def getEACBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 525600.0, 10000.0)

#einstenium
def getEMC2Block():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount <= 144000:
		return 524.305
	elif blockCount <= 288000:
		return 269.585
	elif blockCount <= 432000:
		return 142.225
	elif blockCount <= 576000:
		return 78.545
	elif blockCount <= 864000:
		return 46.705
	elif blockCount <= 1152000:
		return 30.785
	elif blockCount <= 1584000:
		return 22.825
	elif blockCount <= 2304000:
		return 18.845
	elif blockCount <= 5256000:
		return 16.855
	else:
		return 15.86

#elacoin
def getELCBlock():
	return 0
	#very difficult to calculate

#elephantcoin
def getELPBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 3153600.0, 55)

#emerald
def getEMDBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 3153600.0, 5)

#execoin
def getEXEBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 840000.0, 50)

#ezcoin
def getEZCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 844000.0, 50)

#fastcoin
def getFSTBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 2592000.0, 32)

#feathercoin
def getFTCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 840000.0, 200)

#fedoracoin
def getTIPSBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount < 52000:
		return 2500000
	elif blockCount < 104000:
		return 1250000
	elif blockCount < 208000:
		return 625000
	elif blockCount < 416000:
		return 312500
	elif blockCount < 832000:
		return 156250
	elif blockCount < 1664000:
		return 78125
	else:
		return 50000

#flappycoin
def getFLAPBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount < 600000:
		return genBlockReward(blockCount, 100000.0, 500000.0)
	else:
		return 50

#florincoin
def getFLOBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 800000.0, 100.0)

#fluttercoin
def getFLTBlock():
	pass
	#PoT?

#franko
def getFRKBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 22471626.0, 0.25)

#freicoin
def getFRCBlock():
	pass
	#uhh not sure what to think

#global coin
def getGLCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 280000.0, 50.0)

#grandcoin
def getGDCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 700800.0, 1009.487)

#heavycoin
def getHVCBlock():
	#sha-256, keccak-512, groestl-512, blake-512
	pass

#hobonickels
def  getHBNBlock():
	#PoS
	pass

#hypercoin
def getHYCBlock():
	return 25

#infinitecoin
def getIFCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 86400.0, 2**19)

#ixcoin
def getIXCBlock():
	return 96

#joulecoin
def getXJOBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	blockCount = genBlockReward(blockCount, 1401600.0, 16.0)

	if blockCount < 0.001:
		return 0.001
	else:
		return blockCount

#junkcoin
def getJKCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount <= 1036800:
		return 51.6
	else:
		blockCount = genBlockReward(blockCount, 1036800.0, 50)
		return blockCount + 0.1

#krugercoin
def getKGCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 4147200.0, 32)

#kittehcoin
def getMEOWBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 200000.0, 50500.0)

#klondike coin
def getKDCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount < 127776:
		return 16
	elif blockCount < 170976:
		return 8
	elif blockCount < 2273376:
		return 4
	elif blockCount < 3324576:
		return 2
	elif blockCount < 4901376:
		return 1
	elif blockCount < 5506176:
		return 0.5
	else:
		return 0

#leafcoin
def getLEAFBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount < 120000:
		return genBlockReward(blockCount, 15000.0, 500000.0)
	else:
		return 3500

#lottodice
def getLOTBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	blockCount = genBlockReward(blockCount, 259200.0, 32896.0)

	if blockCount < 1:
		return 1
	else:
		return blockCount

#lucky7coin
def getLK7Block():
	#ehhh not sure
	return 0

#lycancoin
def getLYCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 800000.0, 2970.0)

#mastercoin
def getMSTBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount < 1080:
		return 100
	elif blockCount <= 1180:
		return 1
	elif blockCount <= 1380:
		return 2
	elif blockCount <= 1480:
		return 4
	elif blockCount <= 1780:
		return 8
	else:
		return 20

#mazacoin
def getMZCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	blockCount = genBlockReward(blockCount, 241920.0, 5000.0)

	if blockCount < 1:
		return 1
	else:
		return blockCount

#megacoin
def getMECBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	#come back to this

#memecoin
def getMEMEBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 5000.0, 500.0)

#mincoin
def getMNCBlock():
	return 2

#mooncoin
def getMOONBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount <= 300000:
		return genBlockReward(blockCount, 100000.0, 1000000)
	elif blockCount <= 350000:
		return 87500
	elif blockCount <= 375000:
		return 50000
	elif blockCount <= 384400:
		return 25000
	else:
		return 29531

#murraycoin
def getMRYBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 300000.0, 60)

#namecoin
#used bitcoin

#nanotokens
def getNANBlock():
	#know block rewards but not when halving happens
	return 0

#netcoin
def getNETBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	blockCount = genBlockReward(blockCount, 129600.0, 1024.0)

	return blockCount + 134.933

#noirbits
def getNRBBlock():
	return 20

#novacoin
def getNVCBlock():
	pass
	#PoS (proof of stake/piece of shit)

#Nxt
def getNXTBlock():
	pass
	#same as above PoS

#nibble/nybble
def getNBLBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount < 219555:
		return 50
	else:
		return 25

#protoshares
def getPTSBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	blockCount = (blockCount - blockCount % 2016) / 2016

	blockReward = 50

	for i in range(0, blockCount):
		blockReward = blockReward - blockReward * 0.05

	return blockReward

#copperlark
def getCLBlock():
	return 0
	#sha-3 algorithm

#lottery tickets
def getTIXBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount <= 80000:
		return 400000
	elif blockCount <= 160000:
		return 200500
	elif blockCount <= 240000:
		return 151000
	elif blockCount <= 320000:
		return 101500
	elif blockCount <= 400000:
		return 52000
	elif blockCount <= 480000:
		return 27500
	elif blockCount <= 560000:
		return 15500
	elif blockCount <= 600000:
		return 10500
	else:
		return 10000

#nyancoin
def getNYANBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 337000.0, 337)

#orbitcoin
def getORBBlock():
	return 1

#cent
def getCENTBlock():
	return 1
	#not to sure cryptsy does not seem to have it

#philosophersstone
def getPHSBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	blockCount = genBlockReward(blockCount, 64800.0, 64.0)

	return blockCount + 4.9778

#phoenixcoin
def getPXCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 1000000.0, 50.0)

#potcoin
def getPOTBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 840000.0, 420.0)

#peercoin
def getPPCBlock():
	return 90.83471955
	#ill come back to this one

#quark
def getQRKBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	blockCount = genBlockReward(blockCount, 60480.0, 2048.0)

	if blockCount < 1:
		return 1
	else:
		return blockCount

#rabbitcoin
def getRBBTBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	blockCount = genBlockReward(blockCount, 100000.0, 500000.0)

	if blockCount < 10000:
		return 10000
	else:
		return blockCount

#redcoin
def getREDBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 1576800.0, 100.0)

#reddcoin
def getRDDBlock():
	return 0
	#pos velocity

#whitecoin
def getWCBlock():
	return 0
	#pos

#ronpaulcoin
def getRPCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return getblockcount(blockCount, 1051200.0, 1.0)

#royalcoin
def getRYCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 600000.0, 100.0)

#securecoin
def getSRCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 2100000.0, 5.0)

#sexcoin
def getSXCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 600000.0, 100.0)

#smartcoin
def getSMCBlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	if blockCount < 1000:
		return 1
	elif blockCount <= 120000:
		return 64
	else:
		return 16

#spaincoin
def getSPABlock():
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=0000)

	blockCount = conn.getblockcount()

	return genBlockReward(blockCount, 172800.0, 100.0)

#noblecoin
#finish this one
def getNOBLBlock(blockcount):
	if blockcount < 259200:
		return 5000
	elif blockcount < 518400:
		blockcount = blockcount - 259200
		blockcount = ((blockcount / 60) / 24) / 30
		blockReward = 5000
		for x in range(0, int(blockcount)):
			blockReward -= blockReward * 0.01
		return blockReward
	elif blockcount < 777600:
		return 2500
	elif blockcount < 1036800:
		blockcount = blockcount - 259200
		blockcount = ((blockcount / 60) / 24) / 30
		blockReward = 2500
		for x in range(0, int(blockcount)):
			blockReward -= blockReward * 0.01
		return blockReward
	elif blockcount < 1296000:
		return 1250
	elif blockcount < 1555200:
		blockcount = blockcount - 259200
		blockcount = ((blockcount / 60) / 24) / 30
		blockReward = 1250
		for x in range(0, int(blockcount)):
			blockReward -= blockReward * 0.01
		return blockReward
	elif blockcount < 1814400:
		return 625
	elif blockcount < 2073600:
		blockcount = blockcount - 259200
		blockcount = ((blockcount / 60) / 24) / 30
		blockReward = 625
		for x in range(0, int(blockcount)):
			blockReward -= blockReward * 0.01
		return blockReward