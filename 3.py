#!/usr/bin/env python

#
# this happen to work for this problem, but may not cover the general case
#

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
