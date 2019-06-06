from steem.steem import Steem
from send_money import list_load

import logging.config


PRODUCTION = True



logging.config.fileConfig('logging.conf')
logging.basicConfig(filename='1ogs.txt',level=logging.DEBUG)


'''
STEEM blockchain
'''


STEEM_NODES = ['https://steemd.privex.io', 'https://rpc.buildteam.io','https://api.steemit.com']

active_key = list_load("active_wif.txt")
account = list_load("accounts.txt")
ctype = list_load("currency.txt")
amounts = list_load("amounts.txt")


frm_ACCOUNT = "bobinson"
to_ACCOUNT = str(account[0])
amount = amounts[0]

CURRENCY = ctype[0]
print(CURRENCY)

WIF = active_key[0]


# posting, active - fortunex
STEEM_INSTANCE = Steem(keys=[WIF, WIF], nodes=STEEM_NODES, wif=active_key[0])


# END STEEM BLOCKCHAIN

'''
EOS blockchain
'''
