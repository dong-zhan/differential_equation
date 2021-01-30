def dydx(x, t):
	return 9.8-0.196 * x    #DE is from https://tutorial.math.lamar.edu/classes/de/directionfields.aspx
	
def pdf(dydx, xstart, xstop, xnum, ystart, ystop, ynum, xSamples=100, ySamples = 10):		#plot direction field
	global plt, X, Y, U, V, y, t
	
	X, Y = np.meshgrid(np.linspace(xstart, xstop, xnum), np.linspace(ystart, ystop, ynum))
	
	U = 1  
	V = dydx(Y, 0)					#NOTE: it's Y not X.	
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

	plt.show()
	

pdf(dydx, 0, 5, 6, 0, 80, 9)	#this plots his sample DE in direction field
