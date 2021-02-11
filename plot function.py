################ plot function #################
def df(x):
	return x
	
def df(x):
	return np.sin(x)

def pf(df, xstart, xstop, xnum = 50, show = True, linewidth=1.0):		
	global plt, t, s, xstep
	
	xstep = (xstop-xstart)/(xnum)
	
	t = np.arange(xstart, xstop+xstep, xstep)			#use xstop+xstep to include the endpoint.
	s = df(t)
	line, = plt.plot(t, s, linewidth = linewidth)		
	
	if show:
		plt.show()
	
pf(df, 0, np.pi*2)
