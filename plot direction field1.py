################ plot direction field and IVP 1 #################
#most DEs are from https://tutorial.math.lamar.edu/classes/de/directionfields.aspx
def dydx1(x, t):	
	return 9.8-0.196 * x
	
def dydx2(x, t):	
	return (x*x - x - 2)*(1-x)*(1-x)
	
def model1(y,t):
    k = 0.3
    dydt = -k * y
    return dydt
	
def model2(y,t):
    dydt = -y + 1.0
    return dydt
	
def model3(y,t):
    # u steps from 0 to 2 at t=10
    if t<10.0:
        u = 0
    else:
        u = 2
    dydt = (-y + u)/5.0
    return dydt
	
# def model4(z,t):			#doesn't work, pdf needs to be changed accordingly to accept list outputs.
	dxdt = 3.0 * np.exp(-t)
	dydt = -z[1] + 3
	dzdt = [dxdt,dydt]
	return dzdt	
	
def model4x(z,t):			
	dxdt = 3.0 * np.exp(-t)
	return dxdt
	
def model4y(z,t):			
    dxdt = 3.0 * np.exp(-t)
	return dxdt
	
def SeparableEquations1(y, x):
	return 6*y*y*x

def SeparableEquations2(y, x):		
	return (3*x*x + 4*x - 4) / (2*y - 4)
	
def SeparableEquations3(y, x):
	return x*y*y*y / np.sqrt(1+x*x)
	
def SeparableEquations4(y, x):
	return np.exp(-y) * (2*x - 4)
	
def SeparableEquations5(y, x):
	return y*y/x
	
def Exact2(y, x):		
	return (9*x*x-2*x*y)/(2*y+x*x+1)
	
def Exact3(y, x):
	return (2*x*y*y + 4) / (2*(3-x*x*y))
	
def Exact4(y, t):
	return (2*t - 2*t*y/(t*t+1))/-(2-np.log(t*t+1))
	
def Bernoulli1(y, x):
	return (x*x*x*y*y - 4*y/x)
	
def Bernoulli2(y, x):			#(76)
	return (5*y + np.exp(-2*x) / (y*y))
	
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
	
#parameters corresponds to the dydx functions defined on top
pdf(dydx1, 0, 5, 22, 0, 80, 22, 0, 100, 0, 80, 10)
pdf(dydx2, 0, 5, 22, -2, 3, 22, 0, 100, -2, 2, 60)
pdf(model1, 0, 20, 22, 0, 5, 22, 0, 100, 2.5, 7.5, 10)
pdf(model2, 0, 5, 22, 0, 1, 22, 0, 100, 0, 1, 10)
# pdf(model3, 0, 40, 22, 0, 2, 22, 0, 100, 0, 2, 10)
# pdf(model4, 0, 5, 22, 0, 3, 22, 100, 0, 5, 10)

#about initial condition, that y is for the first x
pdf(SeparableEquations1, -3, 3, 22, 0, 1, 22, 1, 100, 1/25-0.1/25, 1/25+0.1/25, 11)		#y(1) = 1/25	
pdf(SeparableEquations1, -3, 3, 22, 0, 1, 22, 1, 100, 1/25, 1/25, 1)
pdf(SeparableEquations2, -4, 4, 22, -1, 12, 22, 1, 100, 2, 4, 11)
pdf(SeparableEquations2, -4, 4, 22, -1, 12, 22, 1, 100, 3, 3, 1)		#y(1) = 3
pdf(SeparableEquations3, -1, 1, 22, -3, 0, 22, 0, 100, -1.5, -0.5, 5)
pdf(SeparableEquations3, -1, 1, 22, -3, 0, 22, 0, 100, -1, -1, 1)	#y(0) = -1
pdf(SeparableEquations4, 0, 10, 22, -10, 4, 22, 5, 100, 0, 0, 1)	#y(5) = 0
pdf(SeparableEquations5, 0, 1.6, 22, 0, 16, 22, 1, 100, 1, 3, 11)
pdf(SeparableEquations5, 0, 1.6, 22, 0, 16, 22, 1, 100, 2, 2, 1)	#y(1) = 2

pdf(Exact2, -2, 6, 22, -50, 0, 22, 0, 100, -4, -2, 6)		
pdf(Exact2, -2, 6, 22, -50, 0, 22, 0, 100, -3, -3, 1)		#y(0) = -3
pdf(Exact3, -5, 0, 22, 0, 30, 22, -1, 100, 7, 9, 5)	
pdf(Exact3, -5, 0, 22, 0, 30, 22, -1, 100, 8, 8, 1)		#y(-1) = 8
pdf(Exact4, 0, 10, 22, -400, 100, 22, 5, 100, -1, 1, 11)		
pdf(Exact4, 0, 10, 22, -400, 100, 22, 5, 100, 0, 0, 1)			#y(5) = 0

pdf(Bernoulli1, 0, 4, 22, -20, 0, 22, 2, 100, -1.5, 0.5, 5)
pdf(Bernoulli1, 0, 4, 22, -20, 0, 22, 2, 100, -1, -1, 1)		#y(2) = -1
pdf(Bernoulli2, -2, 0.5, 22, -2, 10, 22, 0, 100, 1, 3, 11)
pdf(Bernoulli2, -2, 0.5, 22, -2, 10, 22, 0, 100, 2, 2, 1)		#y(0) = 2
