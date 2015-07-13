
from decimal import *
import sys
import bitcoinrpc


def get_number_of_sha_coins(blockReward, hashRate, coin_port=None):
	conn = bitcoinrpc.connect_to_remote('owltest', 'testing', host='127.0.0.1', port=coin_port)

	difficulty = conn.getdifficulty()

	return 20.11624 * blockReward * hashRate / (difficulty * 1000000.0)

def get_number_of_scrypt_coins(blockReward, hashRate, coin_port=None):
	conn = bitcoinrpc.connect_to_remote('owltest', 'dgsjkbksbJFg87qAiFBbgf9', host='127.0.0.1', port=coin_port)

	difficulty = conn.getdifficulty()

	return blockReward/(Decimal(difficulty) * Decimal(49710.26963) / hashRate)

def get_number_of_x11_coins(blockReward, hashRate, coin_port=None):
	conn = bitcoinrpc.connect_to_remote('owltest', 'testing', host='127.0.0.1', port=coin_port)

	difficulty = conn.getdifficulty()

	return (86400.0 * blockReward * hashRate)/(difficulty * 4294967296)

def get_number_of_groestls_coins(blockReward, hashRate, coin_port=None):
	conn = bitcoinrpc.connect_to_remote('owltest', 'testing', host='127.0.0.1', port=coin_port)

	difficulty

	return 86400.0 / (difficulty * 2**32 / hashRate)
