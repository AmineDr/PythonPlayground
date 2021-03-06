from os import system
from web3 import eth
from random import choice
from threading import Thread as th

l = []
attempts = 0
rich_list = []

for x in range(16):
	l.append(hex(x)[2:])

with open('richlist', 'r') as f:
	rich_list = f.readlines()
	for x, y in enumerate(rich_list):
		rich_list[x] = y[:42]
		rich_list[x] = y.lower()

def gen_key():
	key = ''
	for x in range(64):
		key += str(choice(l))
	return key


def get_addr(key):
	return eth.Eth.account.privateKeyToAccount(key).address


def log(text):
	print(str(text), end='\r')


def main():
	global attempts
	attempts_str = ''
	while True:
			key = gen_key()
			addr = get_addr(key).lower()
			for x in rich_list:
				if x == addr:
					with open('rich_list.txt', 'w') as f:
						f.write(key)
					while True:
						print(key)

			attempts += 1
			if attempts > 10**9:
				attempts_str = str(round(attempts/10**9), 1)+ ' B'
			elif attempts > 1000000:
				attempts_str = str(round(attempts/10**6, 1))+ ' M'
			elif attempts > 1000:
				attempts_str = str(round(attempts/1000, 1))+' K'
			else:
				attempts_str = str(attempts)

			log('{} : {}'.format(addr,  attempts_str))

for x in range(100):
	th(target=main).start()
