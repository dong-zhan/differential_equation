################ plot direction field and IVP 1 #################
#most DEs are from https://tutorial.math.lamar.edu/classes/de/directionfields.aspx

#about initial condition, that y is for the first x
def pdf(dydx, xstart, xstop, xnum, ystart, ystop, ynum, x0, xSamples, ySampleStart, ySampleStop, ySamples):		#plot direction field
	global plt, X, Y, U, V, y, t
	
	totalX = xstop - xstart
	if totalX == 0:
		xSamples0 = 1
		xSamples1 = 1
	else:
		ratio = (x0-xstart)/totalX
		xSamples0 = int(xSamples * ratio)
		xSamples1 = int(xSamples - xSamples0)
		
	X, Y = np.meshgrid(np.linspace(xstart, xstop, xnum), np.linspace(ystart, ystop, ynum))
	
	U = 1
	V = dydx(Y, X)					
	N = np.sqrt(U ** 2 + V ** 2)
	U = U/N
	V = V/N
	
	plt.figure()
	plt.title('direction field')
	Q = plt.quiver(X, Y, U, V, angles="xy")			#'xy': Arrows point from (x,y) to (x+u, y+v).
	
	#print(xstart, x0, xSamples0)
	t = np.linspace(x0, xstart, xSamples0)
	for y0 in np.linspace(ySampleStart, ySampleStop, ySamples):
		y = odeint(dydx, y0, t)
		line, = plt.plot(t, y)
		
	#print(t)
	
	t = np.linspace(x0, xstop, xSamples1)
	for y0 in np.linspace(ySampleStart, ySampleStop, ySamples):
		y = odeint(dydx, y0, t)
		line, = plt.plot(t, y)
		
	plt.xlim([xstart, xstop])
	plt.ylim([ystart, ystop])
	plt.xlabel('t')
	plt.ylabel('y(t)')
	
	plt.show()
	

