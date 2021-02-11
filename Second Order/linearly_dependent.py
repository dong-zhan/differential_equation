def f(x) :
	global c
	return c * 9 * np.cos(2*x)
	
def g(x):
	global k
	a = np.cos(x)
	b = np.sin(x)
	return k * (2*a*a - 2*b*b)
	
def test():
	global c, k
	c = 2/9
	k = 1
	pf(f, -2, 2, 50, False, 5)
	pf(g, -2, 2, 50, True, 1)