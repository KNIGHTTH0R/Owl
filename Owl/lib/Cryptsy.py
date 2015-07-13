from decimal import *
import json
import urllib2

def get_market_info():
    marketData = urllib2.urlopen(urllib2.Request('http://pubapi.cryptsy.com/api.php?method=marketdatav2'))

    response = json.loads(marketData.read())

    exchangeInfo = {}
    coinInfo = {}

    for key in response.iterkeys():
        returnDict = response[key]
        if isinstance(returnDict, dict):
            for returnKey in returnDict.iterkeys():
                marketbook = returnDict[returnKey]
                if isinstance(marketbook, dict):
                    for marketKey, marketData in marketbook.iteritems():
                        coinInfo = {"marketid":marketData["marketid"], "price":marketData["lasttradeprice"], "secondarycode":marketData["secondarycode"]}
                        exchangeInfo[marketData['primarycode']] = coinInfo
    return exchangeInfo