################ plot direction field 2 #################
def dydx(x, t):
	return (x*x - x - 2)*(1-x)*(1-x)
	
	
def pdf(dydx, xstart, xstop, xnum, ystart, ystop, ynum, xSamples, ySamples):		#plot direction field
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
	for y0 in ySamples:
		y = odeint(dydx, y0, t)
		line, = plt.plot(t, y, lw=2)
		
	plt.xlim([xstart, xstop])
	plt.ylim([ystart, ystop])
	plt.xlabel('t')
	plt.ylabel('y(t)')
	
	plt.show()
	

def test():
	ys = [-30, -20, -10, -2, -1, 0, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98, 1, 1.3, 1.6, 1.9, 1.92, 1.94, 1.96, 1.98, 2]
	ys = np.array(ys)
	pdf(dydx, 0, 5, 22, -2, 3, 22, 100, ys)	
