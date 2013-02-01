#!/usr/bin/env python


def fibbish(a, b):
	return a + b


p1 = 1
p2 = 2
sum = 2
while p2 < 4000000:
	new = fibbish(p1, p2)
	if new%2 == 0:
		sum += new
	p1 = p2
	p2 = new

print sum
