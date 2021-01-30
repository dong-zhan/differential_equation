################ plot direction field #################
def dydx(x, t):
	return x
	
def dydx(x, t):
	return 9.8-0.196 * x
	
def pdf(dydx, xstart, xstop, xnum, ystart, ystop, ynum):		#plot direction field
	global plt, X, Y, U, V
	
	X, Y = np.meshgrid(np.linspace(xstart, xstop, xnum), np.linspace(ystart, ystop, ynum))
	
	U = 1.0							
	V = dydx(X, 0)					
	N = np.sqrt(U ** 2 + V ** 2)
	U = U/N
	V = V/N

	plt.figure()
	plt.title('direction field')
	Q = plt.quiver(X, Y, U, V, angles="xy")			#'xy': Arrows point from (x,y) to (x+u, y+v).

	plt.show()
	

pdf(dydx, -5, 5, 20, -10, 10, 20)
pdf(dydx, 0, 5, 6, 0, 80, 9)
