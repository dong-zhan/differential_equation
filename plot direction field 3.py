################ plot direction field 3 #################
def dydx3(y, x):		#DE is from https://tutorial.math.lamar.edu/classes/de/directionfields.aspx
	return y - x
	
def pdf3(dydx, xstart, xstop, xnum, ystart, ystop, ynum, xSamples, ySamples):		#plot direction field
	global plt, X, Y, U, V, y, t
	
	X, Y = np.meshgrid(np.linspace(xstart, xstop, xnum), np.linspace(ystart, ystop, ynum))
	
	U = 1  
	V = dydx(Y, X)					#NOTE: it's Y not X.	
	N = np.sqrt(U ** 2 + V ** 2)
	U = U/N
	V = V/N

	plt.figure()
	plt.title('direction field')
	Q = plt.quiver(X, Y, U, V, angles="xy")			#'xy': Arrows point from (x,y) to (x+u, y+v).
	
	t = np.linspace(xstart, xstop, xSamples)
	for y0 in np.linspace(ystart, ystop, ySamples):
		y = odeint(dydx, y0, t)
		line, = plt.plot(t, y, lw=2)
		
	plt.xlim([xstart, xstop])
	plt.ylim([ystart, ystop])
	plt.xlabel('t')
	plt.ylabel('y(t)')
	
	plt.show()
	

pdf3(dydx3, -2, 2, 22, -2, 2, 22, 100, 22)	
