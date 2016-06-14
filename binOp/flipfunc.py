#  1.diff_half_same 2.diff_half_diff 3.not_diff_all 4.diffAll

import numpy as np
import random
import copy

# flip one bit
flip = lambda bit: 0 if bit == 1  else 1

#flip all bits
flipAll = lambda v: [flip(x) for x in v]

#flip half where diff
def flipHalfDiff(v1, v2): # v1, v2 - lists
	diff = []
	for i in range(len(v1)):
		if v1[i] != v2[i] : diff.append(i)
	
	if diff != []:	
		halfDiff = np.random.choice(diff, len(diff) / 2, False)

		newV = copy.copy(v1)
		for i in halfDiff:
			newV[i] = flip(newV[i])
		return newV
	else: return -1
	
#flip some bits	
def flipBits(v1, v2, m, l): # v1, v2 - list; m - same/diff 
	if m != []:	 
		d = np.random.choice(m, l, False)

		newV = copy.copy(v1)
		for i in d:
			newV[i] = flip(newV[i])
		return newV
	else: return -1


#flip half where same
def flipHalfSame(v1, v2): # v1, v2 - lists
	same = []
	for i in range(len(v1)):
		if v1[i] == v2[i] : same.append(i)
	
	halfSame = np.random.choice(same, len(same) / 2, False)

	newV = copy.copy(v1)
	for i in halfSame:
		newV[i] = flip(newV[i])
	return newV