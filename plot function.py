################ plot function #################
def df(x):
	return x
	
def df(x):
	return np.sin(x)

def pf(df, xstart, xstop, xnum = 50):		
	global plt, t, s
	
	xstep = (xstop-xstart)/(xnum-1)
	
	t = np.arange(xstart, xstop, xstep)
	s = df(t)
	line, = plt.plot(t, s, lw=2)

	plt.show()
	
pf(df, 0, np.pi*2)
