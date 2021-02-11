# phase portrait: # dc_ex1
# this plot the trajectory, direction field is plotted with plot direction field1.py

c1 = 1
c2 = 0.5
	
def fx(t):
	global c1, c2
	return -1 * c1 * np.exp(-t) + 2 * c2 * np.exp(4*t)
	
def fy(t):
	global c1, c2
	return 1 * c1 * np.exp(-t) + 3 * c2 * np.exp(4*t)
	
def pf(fx, fy, xstart, xstop, ystart, ystop, num):		
	global plt, X, Y
	
	xstep = (xstop-xstart)/(num)
	tx = np.arange(xstart, xstop+xstep, xstep)		#use xstop+xstep to include the endpoint.
	X = fx(tx)
	
	ystep = (ystop-ystart)/(num)
	ty = np.arange(ystart, ystop+ystep, ystep)
	Y = fy(ty)
	
	line, = plt.plot(X, Y)		

	plt.show()
	
pf(fx, fy, -1, 1, -1, 1, 22)
