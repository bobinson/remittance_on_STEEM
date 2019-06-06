import logging # This module is thread safe.
import time
import os, sys, csv
from datetime import date, timedelta
import steem
import ast
import random
import config


def list_load(listfile: object) -> object:
    with open(listfile, 'r') as readstuff:
        listvar = []
        reader = csv.reader(readstuff)

        for rows in reader:
            v = rows[0]
            listvar.append(v)

    return listvar


# TODO:
def send_cash(amount):
    if config.CURRENCY == "STEEM":
        stat = config.STEEM_INSTANCE.transfer(config.to_ACCOUNT, amount, "STEEM", memo="mb", account=config.frm_ACCOUNT)
    if config.CURRENCY == "SBD":
        stat = config.STEEM_INSTANCE.transfer(config.to_ACCOUNT, amount, "SBD", memo="mb", account=config.frm_ACCOUNT)

    return stat



if __name__ == '__main__':
    stat = "ERR0R1"
    while True:
        try:
            stat = send_cash(config.amount)
        except TypeError as te:
            stat = te.args[0]
            if te.args[0] == "'NoneType' object is not iterable":
                pass
        except Exception as e:
            logging.error(repr(e))
        if stat != "ERR0R1":
            logging.info(stat)
            if stat['operations']:
                break
        if stat == "ERR0R1":
            logging.error(stat)
