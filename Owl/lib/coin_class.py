import bitcoinrpc
import time
import json
import urllib2
from BlockCalc import *
from decimal import *

class Coin:

	coin_count = 0
	_scryptHash = 170000
	_nHash = 285
	_shaHash = 0.0
	_janeHash = 390
	_x11Hash = 2000
	_gHash = 4800

	def __init__(self, name='', poolnumber=0, poolurl='', pooluser='', poolpass='', halving=0, BlockCalc='', AlgoType='', marketid='', price=0.0, primarycode='', secondarycode='', port='', blockreward=0.0, minimum=-1):
		self._marketid = marketid
		self._price = price
		self._primarycode = primarycode
		self._secondarycode = secondarycode
		self._blockreward = blockreward
		self._difficulty = 0.0
		self._port = port
		self._name = name
		self._dailycoins = 0.0
		self._poolnumber = poolnumber
		self._AlgoType = AlgoType
		self._blockcount = 0
		self._halving = halving
		self._BlockCalc = BlockCalc  			#if 0 call built in method, if 1 call external, else return initialReward
		Coin.coin_count += 1
		self._poolurl = poolurl
		self._networkhash = 0.0
		self._poolhash = 0.0
		self._pooluser = pooluser
		self._poolpass = poolpass
		self._minimum = minimum
		self._dailybtc = 0.0

	#mutators
	def setPoolURL(self, url):
		self._poolurl = url

	def setPoolUser(self, user):
		self._pooluser = user

	def setPoolPass(self, password):
		self._poolpass = password

	"""
	def setHash(self):
		try:
			pooljson = urllib2.urlopen(urllib2.Request(self._pooljson))
		except Exception, e:
			print 'Pool JSON Request Failed'
			print self._primarycode
			with open("errorlog.txt", "a") as errorlog:
				errorlog.write(time.strftime("%c") + ': Requesting pool JSON Failed: ' + self._primarycode + '\n')
			errorlog.close()

		try:
			response = json.loads(pooljson.read())
		except Exception, e:
			print 'Loading Pool JSON Failed'
			print self._primarycode
			with open("errorlog.txt", "a") as errorlog:
				errorlog.write(time.strftime("%c") + ': Pool JSON Parsing Failed: ' + self._primarycode + '\n')
			errorlog.close()

		for keys in response.iterkeys():
			if keys == 'getpoolstatus':
				self._poolhash = response[keys]['data']['hashrate']
			elif keys == 'hashrate':
				self._poolhash = response[keys][self._primarycode.lower()]
	"""
	def setWalletInfo(self, port):
		try:
			conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='76.10.186.31', port=port)
			try:
				wallet_response = conn.getmininginfo()

				self._difficulty = wallet_response.difficulty
				self._networkhash = wallet_response.networkhashps
				self._blockcount = wallet_response.blocks

			except Exception, e:
				print '---'
				print 'Get Mining Info Failed'
				print e
				print 'Coin: ', self._primarycode
				print 'Port: ', port
				print '---'
				with open("errorlog.txt", "a") as errorlog:
					errorlog.write(time.strftime("%c") + ': Get Mining Info Failed: ' + self._primarycode + '\n')
				errorlog.close()
		except Exception, e:
			print 'Connection Failed\n'
			print self._primarycode
			with open("errorlog.txt", "a") as errorlog:
				errorlog.write(time.strftime("%c") + ': Wallet Connection Failed: ' + self._primarycode + '\n')
			errorlog.close()

	def setMarketid(self, marketid):
		self._marketid = marketid

	def setPrice(self, price):
		self._price = price

	def setPrimary(self, primary):
		self._primarycode = primary

	def setSecondary(self, secondary):
		self._secondarycode = secondary

	def setReward(self):
		self._blockreward = self.calculateBlockReward(self._blockcount, int(self._halving), int(self._blockreward))

	def setPort(self, port):
		self._port = port

	def setName(self, name):
		self._name = name

	def setDailyCoins(self):
		try:
			#sha coins
			if self._AlgoType == '0':
				self._dailycoins = 20.11624 * self._blockreward * _shaHash / (self._difficulty * 1000000.0)
			#scrypt coins
			elif self._AlgoType == '1':
				print 'Calculating Daily Coins for: ', self._name
				print '---'
				print self._blockreward
				print self._difficulty
				print self._scryptHash
				print self._price
				print self._blockcount
				self._dailycoins = Decimal(self._blockreward) / ((self._difficulty * Decimal(49710.26963)) / (Decimal(Coin._scryptHash) * Decimal(1000.0)))
			#scrypt-n coins
			elif self._AlgoType == '2':
				self._dailycoins = (self._blockreward / (self._difficulty * Decimal(49710.26963) / _nHash))
			#scrypt jane coins
			elif self._AlgoType == '4':
				self._dailycoins = self._blockreward / (self._difficulty * Decimal(49710.26963) / _janeHash)
			#x11 coins
			elif self._AlgoType == '3':
				self._dailycoins = (86400.0 * self._blockreward * _x11Hash) / (self._difficulty * 4294967296.0)
			#groestl
			elif self._AlgoType == '5':
				self._dailycoins = 86400.0 / self._difficulty * 2**32 / _gHash
			else:
				print 'Not Mining this coin \n in def setDailyCoins() in coin_class.py'

			print 'Calculating ', self._name, 'daily BTC'
			self._dailybtc = self._dailycoins * Decimal(self._price)
			print 'Daily BTC for ', self._name, 'is: ', self._dailybtc

		except Exception as err:
			print self._primarycode, ":", err
			with open("errorlog.txt", "a") as errorlog:
				errorlog.write(time.strftime("%c") + err.message + self._primarycode + '\n')
			errorlog.close()

	def setPoolNumber(self, poolnumber):
		self._poolnumber = poolnumber

	def setAlgoType(self, AlgoType):
		self._AlgoType = AlgoType

	def setBlockCalc(self, BlockCalc):
		self._BlockCalc = BlockCalc

	#accessors
	def getDifficulty(self):
		return self._difficulty

	def getMarketid(self):
		return self._marketid

	def getPrice(self):
		return self._price

	def getPrimary(self):
		return self._primarycode

	def getSecondary(self):
		return self._secondarycode

	def getReward(self):
		return self._blockreward

	def getPort(self):
		return self._port

	def getName(self):
		return self._name

	def getDailyCoins(self):
		return self._dailycoins

	def getPoolNumber(self):
		return self._poolnumber

	def getAlgoType(self):
		return self._AlgoType

	def getCount(self):
		return coin_count

	def getDailyBTC(self):
		return self._dailybtc

	#Functions
	def crunchNumbers(self):
		self.setWalletInfo(self._port)
		#self.setHash()

		if self._BlockCalc == '0':
			self.setReward()
			if self._blockreward < self._minimum:
				self._blockreward = self._minimum
		elif self._BlockCalc == '1':
			print 'HERE'
			print self._blockcount
			print self._primarycode
			print type(self._blockcount)
			setExternal(self._primarycode, self._blockcount, self._halving, self._blockreward)
		elif self._BlockCalc == '-1':
			pass
		else:
			print 'Error: BlockCalc number not supported.\n-1 = No calculation return initial reward\n0 = default block calculation\n1 = external block calculation'
			with open("errorlog.txt", "a") as errorlog:
				errorlog.write(time.strftime("%c") + 'Error: BlockCalc number not supported.\n-1 = No calculation return initial reward\n0 = default block calculation\n1 = external block calculation')
			errorlog.close()
		self.setDailyCoins()

	def calculateBlockReward(self, blockcount, halving, blockreward):
		blockcount = (blockcount - (blockcount % halving)) / halving

		for i in range(0, int(blockcount)):
			blockreward = blockreward / 2.0

		return blockreward

	def display(self):
		print 'Market ID:', self._marketid
		print 'Price:', self._price
		print 'Primary Code:', self._primarycode
		print 'Secondary Code:', self._secondarycode
		print 'Block Reward:', self._blockreward
		print 'Difficulty:', self._difficulty
		print 'RPC Port:', self._port
		print 'Name:', self._name
		print 'Daily Coins:', self._dailycoins
		print 'Pool Number:', self._poolnumber
		print 'Algorithm number:', self._AlgoType
		print 'Block Count:', self._blockcount
		print 'Halving:', self._halving
		print 'Block Calc Number:', self._BlockCalc
		print 'Pool URL:', self._poolurl
		print 'Network Hashrate:', self._networkhash
		print 'Pool Hashrate:', self._poolhash
		print 'Pool User:', self._pooluser
		print 'Pool Pass:', self._poolpass
		print 'Daily Profit in Bitcoin', self._dailybtc
		print '\n'