from utils import *
import argparse
from basic_math_funcs import *

def readCiphertext(file):
    with open(file, "r") as fi:
        ciphertext = fi.read()
    return ciphertext

def readPrivateKey(file):
    with open(file, "r") as fi:
        d = int(fi.readline())
        n = int(fi.readline())
    return n, d

def decode(n, d, ciphertext, fileOut, base=4): # file PlanintextDecode
	plaintext = ""
	for i in ciphertext:
		# m = MyMath.powMod(MyBase.toInt(i,64),d,n)
		m=powMod(toInt(i,64),d,n)
		c = str(m)
		while len(c) % base != 0:
			c = '0' + c
		x = 0
		while x != len(c):
			a = c[x:x+base]
			x+= base
			plaintext+= chr(int(a))
	with open(fileOut, "w", encoding="utf-8") as fo:
		fo.write(plaintext)
	return plaintext

def main():
	parser = argparse.ArgumentParser(description="Decode ciphertext to plaintext.")
	parser.add_argument("-i","--input", type=str, default="Data/ciphertext.txt", help="The input file contains ciphertext.")
	parser.add_argument("-o","--output", type=str, default="Data/decoded_plaintext.txt", help="The output file contains decoded plaintext.")
	args = parser.parse_args()
	ciphertext = readCiphertext(args.input)
	n,d = readPrivateKey("Data/private_key.txt")
	decode(n,d,ciphertext.split(), args.output)
	print("Decode successfully!")
	

main()