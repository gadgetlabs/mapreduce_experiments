#!/usr/bin/env python

import sys
from collections import defaultdict
import string
from numpy import *

dict_coords = defaultdict(list)

link = lambda a,b: concatenate((a,b[1:]))
edge = lambda a,b: concatenate(([a],[b]))

def qhull(sample):
	def dome(sample,base): 
		h, t = base
		dists = dot(sample-h, dot(((0,-1),(1,0)),(t-h)))
		outer = repeat(sample, dists>0, 0)

		if len(outer):
			pivot = sample[argmax(dists)]
			return link(dome(outer, edge(h, pivot)),
				dome(outer, edge(pivot, t)))
		else:
			return base

	if len(sample) > 2:
	
		axis = []
		for x in sample:
			axis.append(x[0])

		base = take(sample, [argmin(axis), argmax(axis)], 0)
		return link(dome(sample, base),dome(sample, base[::-1]))
	else:
		return sample


for line in sys.stdin:
	line = line.strip()
	
	key, value = line.split('\t', 1)
	
	try:
		# sort into dictionary with a list 
		coords = (x,y) = value.split(':', 1)
	
		coords = [int(x) for x in coords]
	
		dict_coords[key].append(coords)
	except ValueError:
		# Something wasn't right 
		pass

print "######################################################"

for x in dict_coords.items():
	result = qhull(x[1])
	print ""
	print result
