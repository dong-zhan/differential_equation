# phase portrait: # dc_ex1

################ plot direction field for system of DEs #################
def pdf_sys(dxdt, dydt, xstart, xstop, xnum, ystart, ystop, ynum):
	X, Y = np.meshgrid(np.linspace(xstart, xstop, xnum), np.linspace(ystart, ystop, ynum))
	U = dxdt(Y, X)
	V = dydt(Y, X)
	N = np.sqrt(U ** 2 + V ** 2)
	U = U/N
	V = V/N
	
	plt.figure()
	plt.title('direction field')
	Q = plt.quiver(X, Y, U, V, angles="xy")	

	plt.xlim([xstart, xstop])
	plt.ylim([ystart, ystop])
	plt.show()
	

# dc_ex1
def dxdt(y, x):
	return x+2*y

def dydt(y, x):
	return 3*x+2*y
	
pdf_sys(dxdt, dydt, -10, 10, 22, -10, 10, 22)

################ this plots the trajectory ################
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
