#!/usr/bin/env python

lengths = {1:1}

def next_number(n):
	if n % 2 == 0:
		return n//2
	return n*3 + 1

def collatz(n):
	#if n == 1:
		#return 1
	if n in lengths:
		return lengths[n]
	next_n = next_number(n)
	
	length = 1 + collatz(next_n)
	lengths[n] = length
	return length

for i in xrange(1, 1000001):
	collatz(i)

print max((v,k) for (k,v) in lengths.iteritems())
