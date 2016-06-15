from binary import * 
from stats import *

T, mas = genT()

f = open('data.csv', 'w')
for tt in T:
	f.write(str(tt.k)+ "," + str(tt.l) + "\n")
f.write("# end of file")
f.close()

showPlt()