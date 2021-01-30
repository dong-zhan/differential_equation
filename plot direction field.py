################ plot direction field #################
def func(x, y):
	return np.exp(-(x*x+y*y)) * (1-2*x*x), -2*y*x*np.exp(-(x*x+y*y))

def pd(func, xstart, xstop, xnum, ystart, ystop, ynum):		#plot direction field
	global plt, X, Y, U, V, y, t
	
	X, Y = np.meshgrid(np.linspace(xstart, xstop, xnum), np.linspace(ystart, ystop, ynum))
	
	U, V = func(X, Y)					#NOTE: it's Y not X.
	N = np.sqrt(U*U + V*V)
	U = U/N
	V = V/N
	
	plt.figure()
	plt.title('direction field')
	Q = plt.quiver(X, Y, U, V, angles="xy")			#'xy': Arrows point from (x,y) to (x+u, y+v).
	
	plt.show()
	
pd(func, -2, 2, 22, -2, 2, 22)	
