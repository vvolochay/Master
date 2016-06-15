import sys
from flipfunc import *

class Level: 	
	def __init__(self, inds, masks):
		self.masks = []
		
		if type(inds) == int:
			self.indexes = [inds]
		else: self.indexes = inds
		
		if type(masks) == int:
			self.masks.append([masks])
		else: 
			for m in masks:
				self.masks.append(m)
#				print("masks on this level: ", self.masks)
		
#generating new mask -> after index cutting
# masks exampl: [[0,1], [0,0], [1,0]]; [[0,0,1], [0,1,0],[1,1,0]]
def masksGen(lev, i):
	newMasksList = []
	for m in lev.masks: # m = [1,1,0]
		newM = m[:i]
		newM.append(m[i])
		newM.append(m[i])
		newM.extend(m[i + 1:])
		newMasksList.append(newM)
	return newMasksList
	
#safety mask generating	
def maskFlipGen(masks):
	for x in masks:
		for m in masks[masks.index(x):]:
			newV = flipHalfDiff(x, m)
			if newV == -1: continue
			if masks.count(newV) == 0:   #add it's new 
				masks.append(newV)
				revNewV = flipAll(newV)
				if masks.count(revNewV) == 0: 
					masks.append(revNewV)
	return
		
#cut indexes
def cutIndSet(lev): 
	maxI = max(lev.indexes)
	i = lev.indexes.index(maxI)
	newInd = lev.indexes[:i]
	ni = round(maxI / 2)
	newInd.append(ni)
	newInd.append(maxI - ni)
	newInd.extend(lev.indexes[i + 1:])
	return newInd, i	
		
def nextLevel(prevLev):
	ind, i = cutIndSet(prevLev)
	m = masksGen(prevLev, i)
	maskFlipGen(m)
	return Level(ind, m)	
	
def gen(levels):
	n = int(input())

	l0 = Level(n, [[0], [1]]) # [1] must to be on this level 
	levels.append(l0)  #init 
	
	for lev in levels:
#		print(lev.indexes, lev.masks)
		if max(lev.indexes) > 1: #  [1,1,1... 1,1] -> that's last level
			l = nextLevel(lev)
			levels.append(l)
		else: break
			
levels = [] 
#sys.exit(gen(levels))