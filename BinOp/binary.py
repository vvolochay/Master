from setgen import *
from flipfunc import *

class T:
#	i -> list 
#	j -> list
#	k -> same bits
#	l -> diff bils
#	s -> string from i and j
	k = 0
	s = -1  
	l = 0
	
	def __init__(self, i, j, same, diff):
		self.i = i
		self.j = j
		if same != []:
			self.k = random.randint(1, len(same))
			self.s = flipBits(i, j, same, self.k)
			
		if diff != []:
			self.l = random.randint(1, len(diff))
			self.s = flipBits(i, j, diff, self.l)
	

#for v1 and v2 counted two parameters
def count(v1, v2):
	diff = []
	same = []
	for i in range(len(v1)):
		if v1[i] != v2[i] : diff.append(i)
		else: same.append(i)
	return same, diff	

def genT():	
	levels = []
	gen(levels) 

	n = levels[0].indexes[0]
	
	Tlist = []
	mas = [[] * n] * 2	# [][] - same(e), diff(d)

	for i in levels[len(levels) - 1].masks:
		for j in levels[len(levels) - 1].masks:
			e, d = count(i, j)  # e - same, d - diff 
			t = T(i, j, e, d)
			Tlist.append(t)
#			mas[e][d]#.append(Tlist.index(t))		
	return Tlist, mas

#for s in T:
#	print(s.s)