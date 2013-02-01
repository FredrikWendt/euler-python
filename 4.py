#!/usr/bin/env python

largest = 0
for i in xrange(100,1000):
	for j in xrange(100,1000):
		p = i * j
		if p > largest:
			p_string = str(p)
			p_string_rev = p_string[::-1]
			if p_string == p_string_rev:
				largest = p

print largest
