################ plot function 3D #################
def func(x, y):
	return x*x+y*y
	
def func2(x, y):
	return x*np.exp(-(x*x+y*y))

def imps():
	global plt, cm, LinearLocator, FormatStrFormatter, np
	import matplotlib.pyplot as plt
	from matplotlib import cm
	from matplotlib.ticker import LinearLocator, FormatStrFormatter
	import numpy as np

def pf3d(func, xstart, xstop, xstep, ystart, ystop, ystep, zmin, zmax):
	fig = plt.figure()
	ax = fig.gca(projection='3d')

	# Make data.
	X = np.arange(xstart, xstop, xstep)
	Y = np.arange(ystart, ystop, ystep)
	X, Y = np.meshgrid(X, Y)
	Z = func(X, Y)

	# Plot the surface.
	surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
						   linewidth=0, antialiased=False)

	# Customize the z axis.
	ax.set_zlim(zmin, zmax)
	ax.zaxis.set_major_locator(LinearLocator(10))
	ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

	# Add a color bar which maps values to colors.
	fig.colorbar(surf, shrink=0.5, aspect=5)

	plt.show()
	
pf3d(func, -2, 2, 0.125, -2, 2, 0.125, -5, 5)
pf3d(func2, -2, 2, 0.125, -2, 2, 0.125, -0.5, 0.5)
