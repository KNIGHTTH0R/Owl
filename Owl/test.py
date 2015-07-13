import bitcoinrpc
import json
import urllib2

pooljson = urllib2.urlopen(urllib2.Request('http://fortynyaners.com/index.php?page=api&action=getpoolstatus&api_key=150720ecdde5db85ef14b26ffe406a5b37c9753d63f4d69fb4280f625620b856'))

response = json.loads(pooljson.read())

for keys in response.iterkeys():
	if keys == 'getpoolstatus':
		print 'hashrate: ', response[keys]['data']['hashrate']
	elif keys == 'hashrate':
		print 'hashrate: ' + response[keys]