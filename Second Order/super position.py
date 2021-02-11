def df_d2(x):
	global c1, c2
	return 9 * c1 * np.exp(-3*t) + 9 * c2 * np.exp(3*t)		#very strange here, I used t instead of x, but, it works...
  
def df_solution(t):		
	global c1, c2
	return c1 * np.exp(-3*t) + c2 * np.exp(3*t)
  
def test():
	global c1, c2
	c1 = 0.123
	c2 = 1.345
	pf(df_d2, -1, 1, 50, False)
	pf(df_solution, -1, 1, 50, True)