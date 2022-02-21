# -*- coding: utf-8 -*-

import requests
import json

class CalcVBT(object):
    def __init__(self):
        self.baseUrl = "http://localhost:5003"
        pass

    def get_vbt_value(self, ticker, days, k):
        print ("url :: %s%s?ticker=%s&days=%d" % (self.baseUrl, '/get_ohlcv', ticker, days))
        
        r = requests.get(self.baseUrl + "/get_ohlcv?ticker=%s&days=%d" % (ticker, days))

        value = json.loads(r.json())
        print ('###############################################')
        print (value)
        print (value['close'][list(value['close'])[0]])

        print ('###############################################')

        target_price = value['close'][list(value['close'])[0]] + (value['high'][list(value['high'])[0]] - value['low'][list(value['low'])[0]]) * k
        return target_price