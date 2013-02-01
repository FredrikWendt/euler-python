#!/usr/bin/env python

def sum_of_squares(n):
	total = 0
	for x in xrange(1,n+1):
		total += x*x
	return total

def square_of_sum(n):
	s = sum(xrange(1,n+1))
	return s*s

print sum_of_squares(100) - square_of_sum(100)
