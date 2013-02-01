#!/usr/bin/env python

n = 600851475143
max = n
devisor = 1
for i in xrange(1, n):
	if i > max:
		break
	if max % i == 0:
		max = max / i
		devisor = i

print devisor
