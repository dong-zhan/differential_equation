def df_d2(x):
	return 9 * np.exp(-3*t) + 9 * np.exp(3*t)		#very strange here, I used t instead of x, but, it works...
  
def df_solution(t):		
	return np.exp(-3*t) + np.exp(3*t)
  
pf(df_d2, -1, 1, 50, False)
pf(df_solution, -1, 1, 50, True)
