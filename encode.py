from utils import *
import argparse
from basic_math_funcs import *
def readPlaintext(file):
    with open(file, "r", encoding="utf-8") as fi:
        plaintext = fi.read()
    return plaintext

def getPlaintext(file):
    with open(file, "r", encoding="utf-8") as fi:
        plaintext = fi.read()
    return plaintext

def convertStringToInt(plaintext, base=4):
	result = []
	for i in plaintext:
		c = str(ord(i))
		while len(c) != base:
			c = '0' + c
		result.append(c)
	return result

def createBigInt(R, size_n):
	bitIntList = []
	x = ""
	for i in R:
		if len(x) + len(i) >= size_n: # Tối ưu mã hóa nhiều kí tự nhất có thể
			bitIntList.append(int(x))
			x = ""
		x+= i
	bitIntList.append(int(x))
	return bitIntList

def encode(n, e, plaintext, file):
	ciphertext = ""
	result = convertStringToInt(plaintext) #['0065','0066']
	bitIntList = createBigInt(result, len(str(n))) #[6500660067, 6800690070, 710072]
	for i in bitIntList:
		temp = powMod(i,e,n)
		temp = toBase(temp,64)
		ciphertext+= temp + ' '
	with open(file, "w") as fo:
		fo.write(ciphertext)
	return ciphertext

def readPublicKey(file):
    with open(file, "r") as fi:
        e = int(fi.readline())
        n = int(fi.readline())
    return n, e
def main():
    parser = argparse.ArgumentParser(description="Encode plaintext to ciphertext.")
    parser.add_argument("-i","--input", type=str, default="Data/plaintext.txt", help="The input file contains plaintext.")
    parser.add_argument("-o","--output", type=str, default="Data/ciphertext.txt", help="The output file contains ciphertext.")
    agrs= parser.parse_args()
    plaintext = readPlaintext(agrs.input)
    n,e = readPublicKey("Data/public_key.txt")
    encode(n,e,plaintext, agrs.output)
    print("Encode successfully!")
	
main()


