from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def showPlt():
	thedata = np.genfromtxt(
	                        'data.csv',       # file to read
	                        skip_header=0,      # lines to skip at the top
	                        skip_footer=0,      # lines to skip at the bottom 
	                        delimiter=',',      # column delimiter
	                        dtype='int32'     # data type
	                        )
	                        
	x = thedata[:,0]    # same
	y = thedata[:,1]    # diff

	hist, xedges, yedges = np.histogram2d(x, y, bins=6)

	elements = (len(xedges) - 1) * (len(yedges) - 1)    # number of boxes
	xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
	xpos = xpos.flatten()           # x-coordinates of the bars
	ypos = ypos.flatten()           # y-coordinates of the bars
	zpos = np.zeros(elements)       # zero-array
	dx = 0.5 * np.ones_like(zpos)   # length of the bars along the x-axis
	dy = dx.copy()                  # length of the bars along the y-axis
	dz = hist.flatten()             # height of the bars

	fig = plt.figure()
	ax = Axes3D(fig)

	ax.bar3d(xpos, ypos, zpos,      # lower corner coordinates
	         dx, dy, dz,            # width, depth and height
	         color='cadetblue',      # bar colour
	         alpha=0.6              # transparency of the bars
	         )

	ax.w_xaxis.set_ticklabels([])   
	ax.w_yaxis.set_ticklabels([])   
	ax.set_title('T set distribution')  

	ax.view_init(elev=28, azim=60)  
	ax.dist=12                      

	plt.show()  